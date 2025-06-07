from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Deposito
from .forms import DepositoForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_depositos(request):
    depositos = Deposito.objects.all()
    return render(request, 'deposito/lista.html', {'depositos': depositos})

@login_required
def cadastrar_deposito(request):
    if request.method == 'POST':
        form = DepositoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_depositos')
    else:
        form = DepositoForm()
    return render(request, 'deposito/cadastro.html', {'form': form})

