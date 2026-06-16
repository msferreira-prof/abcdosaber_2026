from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
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
    
def cadastrar(request):
    return render(request, 'titulo/cadastroTitulos.html')

def excluir(request, codigoTitulo):
    titulo = get_object_or_404(Titulo, pk=codigoTitulo)
    titulo.delete()
    
    return redirect('titulo:listar')


def error_404(request, exception):
    return render(request, 'erro404.html', status=404)    

def error_500(request):
    return render(request, 'erro500.html', status=500)    
