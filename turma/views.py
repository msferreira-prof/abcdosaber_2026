from django.http import HttpResponse
from django.shortcuts import redirect, render

from aluno.models import Aluno
from instrutor.models import Instrutor
from tipodeatividade.models import TipoDeAtividade
from turma.forms import AtualizarTurmaForm, TurmaForm
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
    form = TurmaForm(request.POST)
    if form.is_valid():
        dados_turma = form.cleaned_data

        # tipo de atividade
        codigo_atividade = dados_turma['codigo_atividade']
        tipo_de_atividade = TipoDeAtividade.objects.get(pk=codigo_atividade)
        
        # aluno monitor
        matricula_monitor = dados_turma['matricula_monitor']
        monitor = Aluno.objects.get(pk=matricula_monitor)
        
        # instrutor
        id_instrutor = dados_turma['id_instrutor']
        instrutor = Instrutor.objects.get(pk=id_instrutor)
        
        # instanciar objeto Turma do Model
        turma = Turma(
            horario_aula = dados_turma['horario_aula'],
            duracao_aula = dados_turma['duracao_aula'], 
            data_inicial = dados_turma['data_inicial'],
            data_final = dados_turma['data_final'],
            codigo_atividade = tipo_de_atividade,
            matricula_monitor = monitor,
            id_instrutor = instrutor
        )
        
        turma.save()
        return redirect('turma:listar')
        
    else:
        return redirect('turma:carregar_cadastro')


def excluir(request, numero):
    turma = Turma.objects.get(pk=numero)
    turma.delete()
    return redirect('turma:listar')  


def carregar_turma(request, numero):
   
    turma = Turma.objects.get(pk=numero)
    lista_tiposdeatividade = TipoDeAtividade.objects.all()
    lista_instrutores = Instrutor.objects.all()
    lista_alunos = Aluno.objects.all()
    
    contexto = {
        'turma': turma,
        'tiposdeatividade': lista_tiposdeatividade,
        'instrutores': lista_instrutores,
        'alunos': lista_alunos,        
    }
    
    return render(request, 'turma/atualizarTurma.html', context=contexto)

def atualizar(request):
    form = AtualizarTurmaForm(request.POST)
    if form.is_valid():
        dados_turma = form.cleaned_data

        # turma a alterar
        turma = Turma.objects.get(pk=dados_turma['numero'])
        
        turma.horario_aula = dados_turma['horario_aula']
        turma.duracao_aula = dados_turma['duracao_aula']
        turma.data_inicial = dados_turma['data_inicial']
        turma.data_final = dados_turma['data_final']
        
        # tipo de atividade
        if turma.codigo_atividade.codigo != dados_turma['codigo_atividade']:
            turma.codigo_atividade = TipoDeAtividade.objects.get(pk=dados_turma['codigo_atividade'])
        
        # aluno monitor
        if turma.matricula_monitor.matricula != dados_turma['matricula_monitor']:
            turma.matricula_monitor = Aluno.objects.get(pk=dados_turma['matricula_monitor'])
        
        # instrutor
        if turma.id_instrutor != dados_turma['id_instrutor']:
            turma.id_instrutor = Instrutor.objects.get(pk=dados_turma['id_instrutor'])
        
        turma.save()
    
    return redirect('turma:listar')
    
    
def carregar_ausencia(request):
    pass

def carregar_ausencia_alunos(request):
    pass

def registrar_ausencia(request):
    pass

