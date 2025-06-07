from django.urls import path
from . import views

urlpatterns = [
    path('depositos/', views.lista_depositos, name='lista_depositos'),
    path('depositos/novo/', views.cadastrar_deposito, name='cadastrar_deposito'),
]
