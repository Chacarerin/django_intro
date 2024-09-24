from django.urls import path
from .views import *

urlpatterns= [
    path("", index, name="index"),
    path("navbar/", navbar, name="navbar"),
]