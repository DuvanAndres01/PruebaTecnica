# -*- coding: utf-8 -*-
import unicodedata
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.core.cache import cache
from .models import Computador
from .serializers import ComputadorSerializer

# Normalizar texto eliminando tildes, mayúsculas y espacios
def normalizar_texto(texto):
    return unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("utf-8").replace(" ", "").lower()

# Lista de computadores disponibles
class ComputadorListView(generics.ListAPIView):
    queryset = Computador.objects.all()
    serializer_class = ComputadorSerializer

# Chatbot con respuestas dinámicas
class ChatBotView(APIView):
    def post(self, request, *args, **kwargs):
        pregunta = request.data.get('pregunta', '').strip()
        if not pregunta:
            return Response({"error": "La pregunta es requerida."}, status=400)

        pregunta = normalizar_texto(pregunta)  # Normalizar texto

        # Intentar recuperar respuesta en caché
        if (respuesta := cache.get(pregunta)):
            return Response({"respuesta": respuesta})

        # Obtener lista de marcas registradas en la BD
        marcas_disponibles = list(Computador.objects.values_list("marca", flat=True).distinct())
        marcas_normalizadas = {normalizar_texto(marca): marca for marca in marcas_disponibles}

        # Verificar si la pregunta menciona una marca de computadora
        for clave, marca_real in marcas_normalizadas.items():
            if clave in pregunta:
                return self.get_info_computadora(marca_real)

        # Diccionario de respuestas rápidas
        respuestas = {
            "asesor": "Puedes contactar a un asesor llamando al 123-456-7890.",
            "barato": self.get_computador_barato,
            "caro": self.get_computador_caro,
            "grafica": self.get_mejor_grafica,
            "mejorcomputador": self.get_mejor_computador,
            "almacenamiento": self.get_mayor_almacenamiento,
            "ram": self.get_mayor_ram,
        }

        # Buscar palabras clave en la pregunta
        for clave, funcion_respuesta in respuestas.items():
            if clave in pregunta:
                respuesta_final = funcion_respuesta() if callable(funcion_respuesta) else funcion_respuesta
                cache.set(pregunta, respuesta_final, timeout=600)
                return Response({"respuesta": respuesta_final})

        return Response({"respuesta": "No tengo información exacta, pero dime en qué más te puedo ayudar."})

    # Información de computadoras según la marca
    def get_info_computadora(self, marca):
        computadores = Computador.objects.filter(marca=marca).values("nombre", "procesador", "memoria_ram", "almacenamiento", "tarjeta_grafica", "precio")

        if computadores:
            detalles = [f"{compu['nombre']}: {compu['procesador']}, {compu['memoria_ram']}GB RAM, {compu['almacenamiento']}GB, {compu['tarjeta_grafica']}, ${compu['precio']}" for compu in computadores]
            return Response({"respuesta": f"Tenemos estas computadoras {marca}: " + " | ".join(detalles)})
        
        return Response({"respuesta": f"No tenemos computadoras de la marca {marca} disponibles en este momento."})

    # Métodos optimizados para consultas
    def get_computador_barato(self):
        compu = Computador.objects.values("nombre", "precio").order_by("precio").first()
        return f"El computador más barato es {compu['nombre']} con un precio de ${compu['precio']}." if compu else "No hay datos."

    def get_computador_caro(self):
        compu = Computador.objects.values("nombre", "precio").order_by("-precio").first()
        return f"El computador más caro es {compu['nombre']} con un precio de ${compu['precio']}." if compu else "No hay datos."

    def get_mejor_grafica(self):
        compu = Computador.objects.values("nombre", "tarjeta_grafica").order_by("-rendimiento").first()
        return f"El mejor en gráficos es {compu['nombre']} con una {compu['tarjeta_grafica']}." if compu else "No hay datos."

    def get_mejor_computador(self):
        compu = Computador.objects.values("nombre", "rendimiento").order_by("-rendimiento", "-precio").first()
        return f"El mejor computador es {compu['nombre']} con un rendimiento de {compu['rendimiento']}." if compu else "No hay datos."

    def get_mayor_almacenamiento(self):
        compu = Computador.objects.values("nombre", "almacenamiento").order_by("-almacenamiento").first()
        return f"El computador con mayor almacenamiento es {compu['nombre']} con {compu['almacenamiento']}GB." if compu else "No hay datos."

    def get_mayor_ram(self):
        compu = Computador.objects.values("nombre", "memoria_ram").order_by("-memoria_ram").first()
        return f"El computador con más RAM es {compu['nombre']} con {compu['memoria_ram']}GB de memoria." if compu else "No hay datos."
