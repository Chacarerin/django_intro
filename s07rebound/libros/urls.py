from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("inputbook/", formulario, name="formulario"),
]