from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'tipodeatividade/listarTiposAtividade.html')
    
def cadastrar(request):
    return render(request, 'tipodeatividade/cadastroTipoAtividadeTitulos.html')
    