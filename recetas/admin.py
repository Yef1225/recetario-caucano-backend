
from django.contrib import admin
from .models import Receta, Ingrediente


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'municipio_origen', 'tiempo_preparacion')
    search_fields = ('nombre', 'municipio_origen')


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'unidad_medida', 'receta', 'es_opcional')
    list_filter = ('es_opcional', 'receta')
    search_fields = ('nombre',)
