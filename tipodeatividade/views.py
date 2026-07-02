from django.http import HttpResponse
from django.shortcuts import redirect, render
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

def excluir(request, codigo):
    try: 
        tipo_de_atividade = TipoDeAtividade.objects.get(pk=codigo)
        tipo_de_atividade.delete()
    except TipoDeAtividade.DoesNotExist:
        pass
    
    return redirect('tipodeatividade:listar')

