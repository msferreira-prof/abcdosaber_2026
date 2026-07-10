from django.urls import path
from . import views

app_name = 'turma'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.carregar_cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('excluir/<int:numero>', views.excluir, name='excluir'),
    path('carregar_ausencia/', views.carregar_ausencia, name='ausencia'),
    path('carregar_ausencia_alunos/', views.carregar_ausencia_alunos, name='ausencia_alunos'),
    path('registrar_ausencia/', views.registrar_ausencia, name='registrar_ausencia'),
]
