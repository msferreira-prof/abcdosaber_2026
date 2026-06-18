from django.urls import path
from . import views

app_name = 'titulo'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.carregar_cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigoTitulo>', views.excluir, name='excluir_titulo' )
]
