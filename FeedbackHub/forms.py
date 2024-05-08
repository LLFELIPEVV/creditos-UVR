from django import forms

class MensajeForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    tipo = forms.ChoiceField(label='Tipo de mensaje', choices=[('Queja', 'Queja'), ('Sugerencia', 'Sugerencia'), ('Reclamo', 'Reclamo')])
    asunto = forms.CharField(label='Asunto', max_length=100)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea)

