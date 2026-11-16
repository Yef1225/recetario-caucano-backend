from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()
    tiempo_preparacion = models.PositiveIntegerField(help_text="Tiempo en minutos")
    municipio_origen = models.CharField(max_length=80)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.municipio_origen})"
    

class Ingrediente(models.Model):
    receta = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE,
        related_name='ingredientes'
    )

    nombre = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=30)
    es_opcional = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad} {self.unidad_medida})"
