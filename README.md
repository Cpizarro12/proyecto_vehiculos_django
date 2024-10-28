# proyecto_vehiculos_django

## Descripcion
Estado inicial del proyecto

## Tecnologías utilizadas
- VSCode 
- Google Chrome
- Python 3.12.4

## App Vehiculo
- Se utiliza el comando django-admin startapp vehiculo 
- Posteriormente se agrega a installed_apps en el archivo settings.py del proyecto
## Modelo Vehiculo
- Se crea el modelo Vehiculo de la siguiente forma:

```
from django.db import models

class Vehiculo(models.Model):

    MARCAS = [
        ('Fiat','Fiat'),
        ('Chevrolet','Chevrolet'),
        ('Ford','Ford'),
        ('Toyota','Toyota')
    ]

    CATEGORIAS = [
        ('Particular','Particular'),
        ('Transporte','Transporte'),
        ('Carga','Carga'),
    ]


    marca = models.CharField(max_length=20,choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20,choices=CATEGORIAS,default='Particular')
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)   
    fecha_de_modificacion = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.categoria}"
```
## Migraciones
- Se realizan las migraciones con:
```
py manage.py makemigrations
py manage.py migrate
```
## Endpoints
http://127.0.0.1:8000/ --> Index
http://127.0.0.1:8000/vehiculo/add/ -->vehiculo_form