from django.http import HttpResponse
from django.shortcuts import redirect, render
from tipodeatividade.models import TipoDeAtividade
from tipodeatividade.forms import TipoDeAtividadeAtualizarForm, TipoDeAtividadeForm


# Create your views here.
def listar(request):
    lista_tiposdeatividade = TipoDeAtividade.objects.all()
    contexto = {
        'tiposdeatividade': lista_tiposdeatividade
    }
    return render(request, 
                  'tipodeatividade/listarTiposAtividade.html', 
                  context=contexto)

def carregar_cadastro(request):
    return render(request, 'tipodeatividade/cadastroTipoAtividade.html')

def cadastrar(request):
    form = TipoDeAtividadeForm(request.POST)
    if form.is_valid():
        dados_tipo_de_atividade = form.cleaned_data
    
        # verifica se a descricao já foi cadastrada 
        tipo_de_atividade = TipoDeAtividade(
                descricao = dados_tipo_de_atividade['descricao']
        )
        
        tipo_de_atividade.save()
    
    return render(request, 'tipodeatividade/cadastroTipoAtividade.html')


def excluir(request, codigo):
    try: 
        tipo_de_atividade = TipoDeAtividade.objects.get(pk=codigo)
        tipo_de_atividade.delete()
    except TipoDeAtividade.DoesNotExist:
        pass
    
    return redirect('tipodeatividade:listar')


## funcoes para atualizar o tipo de atividade (carregar_tipo_de_atividade e atualizar)
def carregar_tipo_de_atividade(request, codigo):
    # recuperar tipo de atividade a ser atualizado
    tipo_de_atividade = TipoDeAtividade.objects.get(pk=codigo)
    contexto = {
        'tipodeatividade' : tipo_de_atividade
    }
    
    return render(request, 'tipodeatividade/atualizarTipoAtividade.html', context=contexto)


def atualizar(request):
    # verifica se o metodo http é POST
    if request.method == 'POST': 
        # receber form
        form = TipoDeAtividadeAtualizarForm(request.POST)
        # validar form
        if form.is_valid():
            # se ok entao atualiza
            dados_tipo_de_atividade = form.cleaned_data
            
            codigo = dados_tipo_de_atividade['codigo']
            tipo_de_atividade = TipoDeAtividade.objects.get(pk=codigo)
            
            tipo_de_atividade.descricao = dados_tipo_de_atividade['descricao']
            
            tipo_de_atividade.save()
       
    # redirecionar para a lista de titulo
    return redirect('tipodeatividade:listar')

