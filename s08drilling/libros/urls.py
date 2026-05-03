from django.urls import path, include
from .views import *
from .views import registro_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", index, name="index"),
    path('registro/', registro_view, name='registro'),
    path('inputbook/', formulario, name='formulario'),
    path("thanks/", agradecimiento, name = "thanks"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]