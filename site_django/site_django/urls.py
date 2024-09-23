from django.contrib import admin
from django.urls import path
from . import views  # Importa las vistas del proyecto
from Libro import views as libro_views  # Importa las vistas de la app Libro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # URL para la página principal
    path('Libro/', libro_views.libro_home, name='libro_home'),  # URL para la app Libro
]