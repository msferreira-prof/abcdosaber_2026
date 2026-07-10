from django import forms

class TipoDeAtividadeForm(forms.Form):
    descricao = forms.CharField(
        max_length=70,
        required=True,
        help_text='Informe a descrição do Tipo de Atividade'
    )
    
class TipoDeAtividadeAtualizarForm(forms.Form):
    codigo = forms.IntegerField(required=True, help_text='Informe o código do Tipo de Atividade')
    descricao = forms.CharField(max_length=70, required=True, help_text='Informe a descrição do Tipo de Atividade')
    
    