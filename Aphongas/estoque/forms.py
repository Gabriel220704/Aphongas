from django import forms
from .models import Deposito, Fornecedor, Produto, Movimentacao
from django.contrib.auth.models import User
from .models import Movimentacao
from django.contrib.auth.models import User
from django import forms
from django import forms
from .models import Produto, Fornecedor, Deposito
from django import forms
from .models import Movimentacao
from django import forms
from .models import Produto, Movimentacao

class DepositoForm(forms.ModelForm):
    class Meta:
        model = Deposito
        fields = '__all__'

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto', 'quantidade', 'tipo', 'nome_cliente', 'id_fornecedor', 'id_deposito']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']    

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'unidade', 'fornecedor', 'deposito_padrao']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'unidade': forms.Select(attrs={'class': 'form-control'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'deposito_padrao': forms.Select(attrs={'class': 'form-control'}),
        }

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto', 'quantidade', 'tipo', 'nome_cliente', 'id_fornecedor', 'id_deposito']

class FiltroMovimentacaoForm(forms.Form):
    tipo = forms.ChoiceField(
        choices=[('', 'Todos')] + Movimentacao.TIPOS,
        required=False,
        label='Tipo de movimentação'
    )
    produto = forms.ModelChoiceField(
        queryset=Produto.objects.all(),
        required=False,
        label='Produto'
    )
    data_inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Data inicial'
    )
    data_fim = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Data final'
    )