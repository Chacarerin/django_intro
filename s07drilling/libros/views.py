from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm

def index(request):
    return render(request, 'index.html', {})

def formulario(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('/thanks/')  
    else:
        form = BookForm()
    
    return render(request, 'formulario.html', {'form': form})

def agradecimiento(request):
    return render(request, 'thanks.html', {})