from django.urls import path
from .views import simulador

app_name = "Simulador"

urlpatterns = [
    path('Simulador/', simulador, name='Simulador')
]