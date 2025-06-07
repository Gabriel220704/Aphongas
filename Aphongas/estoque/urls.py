from django.urls import path
from . import views

urlpatterns = [
    path('depositos/', views.lista_depositos, name='lista_depositos'),
    path('depositos/novo/', views.cadastrar_deposito, name='cadastrar_deposito'),

    path('fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('fornecedores/novo/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),

    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.cadastrar_produto, name='cadastrar_produto'),
]