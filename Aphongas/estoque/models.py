from django.db import models
from django.contrib.auth.models import User

class Deposito(models.Model):
    descricao = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return self.descricao

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    UNIDADES = [
        ('ml', 'Mililitro'),
        ('lt', 'Litro'),
        ('g', 'Grama'),
        ('kg', 'Quilo'),
        ('m³', 'Metro cúbico'),
    ]
    descricao = models.CharField(max_length=100)
    unidade = models.CharField(max_length=5, choices=UNIDADES)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    deposito_padrao = models.ForeignKey(Deposito, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Produto(models.Model):
    
    descricao = models.CharField(max_length=100)
    unidade = models.CharField(max_length=10)
    id_fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    id_deposito_padrao = models.ForeignKey('Deposito', on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Movimentacao(models.Model):
    TIPOS = [
        ('E', 'Entrada'),
        ('S', 'Saída'),
    ]

    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    nome_cliente = models.CharField(max_length=100, blank=True, null=True)
    id_fornecedor = models.ForeignKey('Fornecedor', on_delete=models.SET_NULL, null=True, blank=True)
    id_deposito = models.ForeignKey('Deposito', on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    dthr_movimentacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.produto} - {self.tipo} - {self.quantidade}'
    



