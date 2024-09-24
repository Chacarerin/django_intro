from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("listbook/", listado, name="listado"),
]