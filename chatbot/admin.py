from django.contrib import admin
from .models import Computador

@admin.register(Computador)
class ComputadorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "marca", "precio", "procesador", "memoria_ram", "almacenamiento", "tarjeta_grafica", "rendimiento")
