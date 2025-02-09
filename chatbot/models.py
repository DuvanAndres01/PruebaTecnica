from django.db import models

class Computador(models.Model):
    nombre = models.CharField(max_length=255)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    procesador = models.TextField()
    memoria_ram = models.IntegerField(help_text="Capacidad en GB")
    almacenamiento = models.IntegerField(help_text="Capacidad en GB")
    almacenamiento_tipo = models.CharField(
        max_length=50, choices=[("HDD", "HDD"), ("SSD", "SSD"), ("Híbrido", "Híbrido")], default="SSD"
    )
    tarjeta_grafica = models.TextField()
    rendimiento = models.FloatField(help_text="Puntuación de rendimiento (1-10)")
    cantidad_disponible = models.IntegerField(default=0, help_text="Cantidad en stock")

    def __str__(self):
        return f"{self.nombre} ({self.marca}) - {self.cantidad_disponible} en stock"
