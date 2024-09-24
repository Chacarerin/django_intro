from django.shortcuts import render
from .services import libros


def index(request):
    return render(request, 'index.html', {})

def listado(request):
    context = {
        "libros": libros
    }
    return render(request, 'listado.html', context)
