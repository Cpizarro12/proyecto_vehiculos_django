from django.shortcuts import render, redirect
from .forms import VehiculoForm
# Create your views here.

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


