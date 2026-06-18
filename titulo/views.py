from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from titulo.forms import TituloForm
from titulo.models import Titulo

# Create your views here.
def listar(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }
    return render(request, 
                  'titulo/listarTitulos.html', 
                  context=contexto)
    
def carregar_cadastro(request):
    contexto = { 
        "status": 0, 
        "mensagem": ""
    }
    return render(request, 'titulo/cadastroTitulos.html', context=contexto)

def cadastrar(request):
    status = 1
    mensagem = "Título cadastrado com sucesso!"
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
    
        # verifica se a descricao já foi cadastrada 
        achou = Titulo.objects.filter(
                descricao__iexact=dados_titulo['descricao'].strip()
            ).exists()
        
        if not achou:
            
            titulo = Titulo(
                descricao = dados_titulo['descricao']
            )
        
            titulo.save()
        else:
            status = 2
            mensagem = "Título já foi cadastrado!"
        
    contexto = {
        "status": status,
        "mensagem": mensagem
    }

    return render(request, 'titulo/cadastroTitulos.html', context=contexto)

def excluir(request, codigoTitulo):
    titulo = get_object_or_404(Titulo, pk=codigoTitulo)
    titulo.delete()
    
    return redirect('titulo:listar')


def error_404(request, exception):
    return render(request, 'erro404.html', status=404)    

def error_500(request):
    return render(request, 'erro500.html', status=500)    
