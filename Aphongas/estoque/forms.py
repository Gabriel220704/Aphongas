from django import forms
from .models import Deposito, Fornecedor, Produto, Movimentacao
from django.contrib.auth.models import User
from .models import Movimentacao

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