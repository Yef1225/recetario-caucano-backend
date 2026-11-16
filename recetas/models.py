from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()
    tiempo_preparacion = models.PositiveIntegerField(help_text="Tiempo en minutos")
    municipio_origen = models.CharField(max_length=80)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.municipio_origen})"