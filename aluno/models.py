from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True, help_text="Informe a matrícula do Aluno")
    nome = models.CharField(
        max_length=70,
        null=False,
        help_text='Informe o nome do Aluno'        
    )
    
    data_inicial = models.DateField(null=False, help_text="Informe a data de inicial de matrícula do Aluno")
    data_final = models.DateField(null=True, blank=True, help_text="Informe a data de final de matrícula do Aluno")
    
    def __str__(self):
        return f'{self.matricula} - {self.nome}'
    