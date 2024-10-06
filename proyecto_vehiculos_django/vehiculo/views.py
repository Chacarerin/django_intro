from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import VehiculoForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Vehiculo 

def index(request):
    context = {}

    return render(request, "index.html", context)

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect(reverse('register'))  
        
        #Creación de usuario:
        
        user = User.objects.create_user(username=email, email=email, password=password1, first_name=first_name, last_name=last_name)
        user.is_active = True
        user.save()

        #Asignar un permiso, en este caso el de "visualizar_catalogo"

        content_type = ContentType.objects.get_for_model(Vehiculo)
        permission = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
        user.user_permissions.add(permission)

        #login del usuario:

        user = authenticate(username=email, password=password1)
        if user is not None:
            login(request, user)
        messages.success(request, 'Usuario creado exitosamente')
        return redirect('index')
    
class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Sesion Iniciada Exitosamente"
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.WARNING, "Sesion Cerrada Exitosamente")
        return response
    
def vehiculoform_view(request):
    context ={}
    form = VehiculoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Vehículo ingresado exitosamente')
        return HttpResponseRedirect('/')
    
    context['form']= form
    return render(request, "vehiculo_add.html", context)

@login_required
def vehiculolist_view(request):
    if not request.user.has_perm('vehiculo.visualizar_catalogo'):
        messages.warning(request, 'No posees los permisos para acceder a este recurso!')
        return HttpResponseRedirect('/')

    lista_vehiculos = Vehiculo.objects.all()
    context = { "vehiculos": lista_vehiculos }
    return render(request, "vehiculo_list.html", context)