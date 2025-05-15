from django.urls import path
from . import views

urlpatterns = [
    path('listar_entradas/', views.listar_entradas, name='listar_entradas'),
    path('cadastrar_entrada/', views.cadastrar_entrada, name='cadastrar_entrada')
]




