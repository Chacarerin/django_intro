from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libros.urls')),  # Incluir las URLs de la app libros
    path('accounts/', include('django.contrib.auth.urls')),  # Incluir las URLs del sistema de autenticación de Django
]
