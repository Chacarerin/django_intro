from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Formulario de registro de usuarios
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Proporcione una dirección de correo válida.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']