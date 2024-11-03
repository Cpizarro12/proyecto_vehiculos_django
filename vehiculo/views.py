from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin 
from django.urls import reverse
from .forms import VehiculoForm
from .models import Vehiculo
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import permission_required

# Create your views here.

class VehiculoFormView(PermissionRequiredMixin,FormView):
    template_name = 'vehiculo_form.html'
    form_class = VehiculoForm

    permission_required = 'Can_add_vehiculo_model'

    def get_success_url(self) -> str:
        return reverse("vehiculo_add")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def handle_no_permission(self):
        return redirect(reverse('index'))

def index(request):
    return render(request, 'index.html')

def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm
    return render(request,'vehiculo_form.html',{'form':form})       


@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    for v in vehiculos:
        if v.precio < 10000:
            v.nivel_precio = "Bajo"
        elif v.precio <= 30000:
            v.nivel_precio = "Medio"
        else:
            v.nivel_precio = "Alto"
    return render(request, 'listar_vehiculos.html', {'vehiculos': vehiculos})
