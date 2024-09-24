from django.urls import path
from .views import *

urlpatterns= [
    path("", index, name="index"),
    path("acerca/", acerca, name="acerca_de")
]