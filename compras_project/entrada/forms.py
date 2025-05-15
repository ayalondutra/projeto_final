from django import forms
from .models import Entrada

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['produto', 'quantidade', 'preco_unitario']


