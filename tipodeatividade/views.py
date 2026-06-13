from django.http import HttpResponse
from django.shortcuts import render
from tipodeatividade.models import TipoDeAtividade

# Create your views here.
def listar(request):
    lista_tiposdeatividade = TipoDeAtividade.objects.all()
    contexto = {
        'tiposdeatividade': lista_tiposdeatividade
    }
    return render(request, 
                  'tipodeatividade/listarTiposAtividade.html', 
                  context=contexto)

def cadastrar(request):
    return render(request, 'tipodeatividade/cadastroTipoAtividade.html')
    