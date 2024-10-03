from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistroUsuarioForm  # Asegúrate de que solo importas lo necesario

def index(request):
    return render(request, 'index.html', {})


def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente tras el registro
            messages.success(request, 'Registro exitoso. Bienvenido al sistema.')
            return redirect('home')  # Redirige a la página de inicio después del registro
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registro.html', {'form': form})