from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Deposito, Fornecedor
from .forms import DepositoForm, FornecedorForm
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages
from .models import Movimentacao, Produto
from .forms import MovimentacaoForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import Produto, Movimentacao
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import ProdutoForm
from django.shortcuts import render
from .models import Produto
from django.shortcuts import render, redirect
from .models import Produto, Fornecedor, Deposito
from .forms import ProdutoForm 
from .models import Movimentacao
from .forms import MovimentacaoForm
from django.contrib.auth.decorators import login_required
from .forms import FiltroMovimentacaoForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
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

@login_required
def relatorio_estoque(request):
    produtos = Produto.objects.all()
    dados_estoque = []

    for produto in produtos:
        entradas = Movimentacao.objects.filter(produto=produto, tipo='E').aggregate(Sum('quantidade'))['quantidade__sum'] or 0
        saidas = Movimentacao.objects.filter(produto=produto, tipo='S').aggregate(Sum('quantidade'))['quantidade__sum'] or 0
        saldo = entradas - saidas

        dados_estoque.append({
            'produto': produto,
            'entradas': entradas,
            'saidas': saidas,
            'saldo': saldo
        })

    return render(request, 'relatorio/estoque.html', {'dados_estoque': dados_estoque})

@login_required
def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all()
    return render(request, 'movimentacao/lista.html', {'movimentacoes': movimentacoes})

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

@user_passes_test(is_admin)
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash da senha
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('lista_usuarios')
    else:
        form = UserForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'estoque/cadastrar_produto.html', {'form': form})


def lista_produtos(request):
    busca = request.GET.get('busca', '')
    if busca:
        produtos = Produto.objects.filter(descricao__icontains=busca)
    else:
        produtos = Produto.objects.all()

    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos, 'busca': busca})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  # redireciona pra lista depois de salvar
    else:
        form = ProdutoForm()
    return render(request, 'estoque/cadastrar_produto.html', {'form': form})

@login_required
def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all().order_by('-dthr_movimentacao')
    return render(request, 'estoque/lista_movimentacoes.html', {'movimentacoes': movimentacoes})

@login_required
def cadastrar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.id_usuario = request.user
            movimentacao.save()
            return redirect('lista_movimentacoes')
    else:
        form = MovimentacaoForm()
    return render(request, 'estoque/cadastrar_movimentacao.html', {'form': form})

@login_required
def relatorio_movimentacoes(request):
    form = FiltroMovimentacaoForm(request.GET or None)
    movimentacoes = Movimentacao.objects.all().order_by('-dthr_movimentacao')

    if form.is_valid():
        tipo = form.cleaned_data.get('tipo')
        produto = form.cleaned_data.get('produto')
        data_inicio = form.cleaned_data.get('data_inicio')
        data_fim = form.cleaned_data.get('data_fim')

        if tipo:
            movimentacoes = movimentacoes.filter(tipo=tipo)
        if produto:
            movimentacoes = movimentacoes.filter(produto=produto)
        if data_inicio:
            movimentacoes = movimentacoes.filter(dthr_movimentacao__date__gte=data_inicio)
        if data_fim:
            movimentacoes = movimentacoes.filter(dthr_movimentacao__date__lte=data_fim)

    return render(request, 'estoque/relatorio_movimentacoes.html', {
        'form': form,
        'movimentacoes': movimentacoes
    })

@login_required
def home(request):
    return render(request, 'estoque/home.html')

def movimentar_produto(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            # lógica de movimentação
            form.save()
            return redirect('lista_movimentacoes')  # ou outro nome de rota
    else:
        form = MovimentacaoForm()
    return render(request, 'estoque/movimentar_produto.html', {'form': form})

