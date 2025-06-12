from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .views import EntradaViewSet

router  = DefaultRouter(trailing_slash=False)
router.register(r'entradas', EntradaViewSet)

urlpatterns = [
    path('listar_entradas/', views.listar_entradas, name='listar_entradas'),
    path('cadastrar_entrada/', views.cadastrar_entrada, name='cadastrar_entrada')
]

urlpatterns += router.urls
