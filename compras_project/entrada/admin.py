from django.contrib import admin
from .models import Entrada

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'preco_unitario', 'data_compra')
    search_fields = ('produto',)
    list_filter = ('data_compra',)
