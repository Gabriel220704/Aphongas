from django.contrib import admin
from .models import Deposito, Fornecedor, Produto, Movimentacao

admin.site.register(Deposito)
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Movimentacao)
