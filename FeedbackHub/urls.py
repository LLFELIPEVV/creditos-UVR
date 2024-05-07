from django.urls import path
from .views import FeedbackHub

app_name = "FeedbackHub"

urlpatterns = [
    path('Comentarios/', FeedbackHub, name='quejas')
]