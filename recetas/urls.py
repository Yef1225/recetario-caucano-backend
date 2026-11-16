
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecetaViewSet, IngredienteViewSet

router = DefaultRouter()

router.register(r'recetas', RecetaViewSet, basename='receta')
router.register(r'ingredientes', IngredienteViewSet, basename='ingrediente')

urlpatterns = [
    path('', include(router.urls)),
]
