from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    valoracion = forms.IntegerField(max_value=10000, min_value=0)
    class Meta:
        model = Book
        fields = "__all__"
      