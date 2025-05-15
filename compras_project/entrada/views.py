from django.shortcuts import render, redirect
from .models import Entrada
from .forms import EntradaForm

def listar_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'listar_entradas.html', {'entradas': entradas})

def cadastrar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_entradas')
    else:
        form = EntradaForm()
    return render(request, 'cadastrar_entrada.html', {'form': form})
