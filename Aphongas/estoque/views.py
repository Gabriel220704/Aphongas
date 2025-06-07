from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Deposito, Fornecedor
from .forms import DepositoForm, FornecedorForm
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages
from .models import Movimentacao, Produto
from .forms import MovimentacaoForm

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

@login_required
def cadastrar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.id_usuario = request.user

            
            if movimentacao.tipo == 'S':
                entradas = Movimentacao.objects.filter(produto=movimentacao.produto, tipo='E').aggregate(models.Sum('quantidade'))['quantidade__sum'] or 0
                saidas = Movimentacao.objects.filter(produto=movimentacao.produto, tipo='S').aggregate(models.Sum('quantidade'))['quantidade__sum'] or 0
                saldo = entradas - saidas

                if movimentacao.quantidade > saldo:
                    messages.error(request, 'Quantidade insuficiente em estoque para saída!')
                    return render(request, 'movimentacao/cadastro.html', {'form': form})

            movimentacao.save()
            messages.success(request, 'Movimentação registrada com sucesso!')
            return redirect('cadastrar_movimentacao')
    else:
        form = MovimentacaoForm()

    return render(request, 'movimentacao/cadastro.html', {'form': form})


