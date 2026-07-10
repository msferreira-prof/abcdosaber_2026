from django.db import models
from django.utils import timezone

from aluno.models import Aluno
from instrutor.models import Instrutor
from tipodeatividade.models import TipoDeAtividade

# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(primary_key=True, help_text="Informe o número da Turma")
    horario_aula = models.TimeField(help_text="Informe a hora de aula da Turma")
    duracao_aula = models.SmallIntegerField(default=4, help_text="Informe a duração da aula da Turma")
    data_inicial = models.DateField(default=timezone.now, help_text="Informe a data inicial da Turma" )
    data_final = models.DateField(null=True, blank=True, help_text="Informe a data final da Turma" )    
    codigo_atividade = models.ForeignKey(
        TipoDeAtividade
        , on_delete=models.CASCADE
        , related_name='atividades')
    matricula_monitor = models.ForeignKey(
        Aluno
        , null=True        
        , on_delete=models.SET_NULL
        , related_name='alunos')
    id_instrutor = models.ForeignKey(
        Instrutor
        , null=True        
        , on_delete=models.CASCADE
        , related_name='instrutores')
    
    def __str__(self):
        return f'Turma: {self.numero}'
    
