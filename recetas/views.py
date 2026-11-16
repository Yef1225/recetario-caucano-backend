
from rest_framework import viewsets
from .models import Receta, Ingrediente
from .serializers import RecetaSerializer, IngredienteSerializer


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().order_by('-fecha_creacion')
    serializer_class = RecetaSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all().order_by('id')
    serializer_class = IngredienteSerializer
