from django.urls import path
from .views import FeedbackHub

urlpatterns = [
    path('Comentarios/', FeedbackHub, name='quejas')
]