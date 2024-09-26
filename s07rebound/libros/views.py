from django.shortcuts import render
from .forms import BookForm

def index(request):
    return render(request, 'index.html', {})

def formulario(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Aquí podrías procesar los datos del formulario
            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            valoracion = form.cleaned_data['valoracion']
            # Procesamiento de los datos, como guardarlos en una base de datos o hacer alguna lógica adicional.
            return render(request, 'formulario.html', {'form': form})
    else:
        form = BookForm()
    
    return render(request, 'formulario.html', {'form': form})
