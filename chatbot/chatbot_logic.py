from .models import Computador

def obtener_inventario():
    computadoras = Computador.objects.all()
    if not computadoras.exists():
        return "No hay computadoras disponibles en este momento."
    
    respuesta = "Actualmente tenemos las siguientes computadoras en stock:\n"
    for pc in computadoras:
        respuesta += f"- {pc.nombre} ({pc.marca}): {pc.cantidad_disponible} disponibles.\n"
    
    return respuesta

def obtener_info_computadora(nombre):
    try:
        pc = Computador.objects.get(nombre__icontains=nombre)
        return f"{pc.nombre} de {pc.marca}: {pc.memoria_ram}GB RAM, {pc.almacenamiento}GB {pc.almacenamiento_tipo}, Procesador {pc.procesador}, Tarjeta gráfica {pc.tarjeta_grafica}."
    except Computador.DoesNotExist:
        return "No encontré información sobre esa computadora."
