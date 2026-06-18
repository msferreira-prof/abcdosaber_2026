from django.http import HttpResponse
from django.shortcuts import render

from instrutor.models import Instrutor

# Create your views here.
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        "instrutores": lista_instrutor
    }
    
    return render(request, 'instrutor/listarInstrutores.html', context=contexto)
    
def cadastrar(request):
    return render(request, 'instrutor/cadastroInstrutor.html')
    