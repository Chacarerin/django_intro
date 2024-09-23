from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, esta es una página de prueba de palindromos. Ingresa la URL /palindromo/'frase'")

urlpatterns = [
    path('palindromo/', include('palindromo.urls')),
    path('', index),
]
