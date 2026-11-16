
from rest_framework import serializers
from .models import Receta, Ingrediente


class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'


class IngredienteSerializer(serializers.ModelSerializer):
    receta_nombre = serializers.ReadOnlyField(
        source='receta.nombre'
    )

    class Meta:
        model = Ingrediente
        fields = [
            'id',
            'receta',
            'receta_nombre',
            'nombre',
            'cantidad',
            'unidad_medida',
            'es_opcional'
        ]
