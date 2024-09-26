# importar la librería estándar de Django Forms
from django import forms
# Creación de un forms
class BookForm(forms.Form):
    titulo = forms.CharField(max_length = 150, label="Título")
    autor = forms.CharField(max_length = 150, label = "Autor")
    valoracion = forms.IntegerField(min_value=0, max_value=10000, label="Valoración")