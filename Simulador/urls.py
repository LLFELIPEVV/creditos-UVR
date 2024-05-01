from django.urls import path
from .views import simulador

urlpatterns = [
    path('Simulador/', simulador, name='Simulador')
]