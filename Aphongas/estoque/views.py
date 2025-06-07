from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Deposito, Fornecedor
from .forms import DepositoForm, FornecedorForm
from .models import Produto
from .forms import ProdutoForm

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

@login_required
def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedor/lista.html', {'fornecedores': fornecedores})

@login_required
def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'fornecedor/cadastro.html', {'form': form})


@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/lista.html', {'produtos': produtos})

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produto/cadastro.html', {'form': form})