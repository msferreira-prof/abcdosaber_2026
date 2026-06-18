from django import forms

class TituloForm(forms.Form):
    descricao = forms.CharField(
        max_length=70,
        required=True,
        help_text='Informe a descrição do Título'
    )
    
    