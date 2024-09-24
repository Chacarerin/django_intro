from django.shortcuts import render
from .services import libros


def index(request):
    return render(request, 'index.html', {})

def navbar(request):
    return render(request, 'navbar.html', {})

def footer(request):
    return render(request, 'footer.html', {})

def listado(request):
    context = {
        "libros": libros
    }
    return render(request, 'listado.html', context)
