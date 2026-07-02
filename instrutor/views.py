from django.http import HttpResponse
from django.shortcuts import redirect, render

from instrutor.forms import InstrutorForm
from instrutor.models import Instrutor
from titulo.models import Titulo

# Create your views here.
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        "instrutores": lista_instrutor
    }
    
    return render(request, 'instrutor/listarInstrutores.html', context=contexto)
    
def cadastrar(request):
    form_instrutor = InstrutorForm(request.POST)
    if form_instrutor.is_valid():
        dados_instrutor = form_instrutor.cleaned_data
        
        titulo = Titulo.objects.get(codigo=dados_instrutor['codigo_titulo'])
        
        instrutor = Instrutor(
            rg = dados_instrutor['rg'],
            nome = dados_instrutor['nome'],
            data_nascimento = dados_instrutor['data_nascimento'],
            ddd = dados_instrutor['ddd'],
            telefone = dados_instrutor['telefone'],
            codigo_titulo=titulo
        )
        
        instrutor.save()
        
        return redirect('instrutor:listar')
    
    else:
        erros = form_instrutor.errors
        contexto = {
            'erros': erros
        }
        
        return render(request, 'instrutor/pagina_erro.html', context=contexto)

    
def carregar_cadastro(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        "titulos": lista_titulos
    }
    
    return render(request, 'instrutor/cadastroInstrutor.html', context=contexto)

def excluir(request, id):
    try: 
        instrutor = Instrutor.objects.get(pk=id)
        instrutor.delete()
    except Instrutor.DoesNotExist:
        pass
    
    return redirect('instrutor:listar')  

