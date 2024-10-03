from django.urls import path
from .views import *
from .views import registro_view

urlpatterns = [
    path("", index, name="index"),
    path('registro/', registro_view, name='registro'),
    
]