from django import forms

class SimuladorForm(forms.Form):
    monto_credito = forms.FloatField(label='Monto del crédito')
    tasa_anual = forms.FloatField(label='Tasa de interés anual')
    plazo_credito = forms.IntegerField(label='Plazo del crédito (en meses)')
    mes_pago = forms.IntegerField(label='Numero de cuota (ejemplo: 2 si es la segunda cuota que va a pagar)')
