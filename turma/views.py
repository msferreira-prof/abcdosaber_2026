from django.http import HttpResponse
from django.shortcuts import redirect, render

from aluno.models import Aluno
from instrutor.models import Instrutor
from tipodeatividade.models import TipoDeAtividade
from turma.models import Turma

# Create your views here.
def listar(request):
    lista_turmas = Turma.objects.all()
    contexto = {
        'turmas': lista_turmas
    }
    
    return render(request, 'turma/listarTurmas.html', context=contexto)


def carregar_cadastro(request):
    lista_tiposdeatividade = TipoDeAtividade.objects.all()
    lista_instrutores = Instrutor.objects.all()
    lista_alunos = Aluno.objects.all()
    
    contexto = {
        'tiposdeatividade': lista_tiposdeatividade,
        'instrutores': lista_instrutores,
        'alunos': lista_alunos,        
    }
    
    return render(request, 'turma/cadastroTurma.html', context=contexto)


def cadastrar(request):
    pass

def excluir(request, numero):
    turma = Turma.objects.get(pk=numero)
    turma.delete()
    return redirect('turma:listar')  


def carregar_ausencia(request):
    pass

def carregar_ausencia_alunos(request):
    pass

def registrar_ausencia(request):
    pass

