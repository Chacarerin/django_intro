from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html', {})

def navbar(request):
    
    return render(request, 'navbar.html', {})

def acerca(request):

    return render(request, 'acerca.html', {})