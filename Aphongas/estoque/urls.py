from django.urls import path
from . import views

urlpatterns = [
    path('depositos/', views.lista_depositos, name='lista_depositos'),
    path('depositos/novo/', views.cadastrar_deposito, name='cadastrar_deposito'),

    path('fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('fornecedores/novo/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),

    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.cadastrar_produto, name='cadastrar_produto'),
    
    path('movimentacao/novo/', views.cadastrar_movimentacao, name='cadastrar_movimentacao'),
    path('movimentacao/', views.lista_movimentacoes, name='lista_movimentacoes'),

    path('relatorio/estoque/', views.relatorio_estoque, name='relatorio_estoque'),

    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/novo/', views.cadastrar_usuario, name='cadastrar_usuario'),

    path('produtos/novo/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),

    path('movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('movimentacoes/nova/', views.cadastrar_movimentacao, name='cadastrar_movimentacao'),
    
    path('relatorio/', views.relatorio_movimentacoes, name='relatorio_movimentacoes'),

    path('', views.home, name='home'),
    path('movimentar/', views.movimentar_produto, name='movimentar_produto'),

]

