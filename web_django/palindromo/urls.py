from django.urls import path
from . import views

urlpatterns = [
    path('<str:frase>', views.es_palindromo, name='es_palindromo'),
]