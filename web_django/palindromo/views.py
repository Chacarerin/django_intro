from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def es_palindromo(request, frase):
    frase_limpia = ''.join(frase.split()).lower()
    if frase_limpia == frase_limpia[::-1]:
        resultado = "ES PALINDROMO"
    else:
        resultado = "NO ES PALINDROMO"
    return HttpResponse(f"{frase} {resultado}")