from django.urls import path
from tipodeatividade import views

app_name = 'tipodeatividade'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.carregar_cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigo>', views.excluir, name='excluir_tipodeatividade'),
    path('carregar_tipodeatividade/<int:codigo>', views.carregar_tipo_de_atividade, name='carregar_tipodeatividade'),
    path('atualizar/', views.atualizar, name='atualizar_tipodeatividade'),
]


