from django.urls import path
from . import views

urlpatterns = [
    
    path("add/",views.add_vehiculo ,name="vehiculo_add"),
    path('listar/', views.listar_vehiculos, name='listar_vehiculos'),    
]
