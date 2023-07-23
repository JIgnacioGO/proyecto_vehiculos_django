from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import VehiculoForm
from .models import Vehiculo


# Create your views here.

# Vista de la página principal de la aplicación
def index(request):
    return render(request, 'vehiculo/index.html')


# Vista para agregar un nuevo vehículo
@login_required
@permission_required('vehiculo.agregar_vehiculo', login_url='/accounts/login/')
def vehiculo_add(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo:index')
    else:
        form = VehiculoForm()

    return render(request, 'vehiculo/vehiculo_add.html', {'form': form})


# Vista para listar los vehículos
@login_required
@permission_required('vehiculo.visualizar_catalogo')
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/vehiculo_list.html', {'vehiculos': vehiculos})


# Vista para registro de usuario
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vehiculo:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


