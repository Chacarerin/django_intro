from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book

# Formulario de registro de usuarios
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Proporcione una dirección de correo válida.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BookForm(forms.ModelForm):
    valoracion = forms.IntegerField(max_value=10000, min_value=0)
    class Meta:
        model = Book
        fields = "__all__"