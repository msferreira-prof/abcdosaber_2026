from django import forms
from django.utils import timezone

class TurmaForm(forms.Form):
    horario_aula = forms.TimeField(required=True, help_text="Informe a hora de aula da Turma")
    duracao_aula = forms.IntegerField(required=True, initial=4, help_text="Informe a duração da aula da Turma")
    data_inicial = forms.DateField(required=True, help_text="Informe a data inicial da Turma" )
    data_final = forms.DateField(required=False, help_text="Informe a data final da Turma" )    
    codigo_atividade = forms.IntegerField(required=True, help_text="Informe o código do Tipo de Atividade da Turma")
    matricula_monitor = forms.IntegerField(required=True, help_text="Informe a matrícula do Aluno Monitor da Turma")
    id_instrutor = forms.IntegerField(required=True, help_text="Informe o id do Instrutor da Turma")
    
    