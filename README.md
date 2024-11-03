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
## Crear las vistas y urls en la app vehiculo
- proyecto_vehiculos_django\vehiculo\views.py
- proyecto_vehiculos_django\vehiculo\forms.py
- proyecto_vehiculos_django\vehiculo\urls.py
- proyecto_vehiculos_django\vehiculo\templates\vehiculo_form.html


## Endpoints
http://127.0.0.1:8000/ --> Index
http://127.0.0.1:8000/vehiculo/add/ -->vehiculo_form



## Agregar los siguientes Vehículos:
| Marca     | Modelo           | Serial carroceria | Serial motor | Categoria  | Precio |
|-----------|------------------|-------------------|--------------|------------|--------|
| Fiat      | Punto            | 254AADD           | 4521475      | Particular | 9200   |
| Fiat      | Furgoneta Ducato | 25ED235           | 8554122      | Transporte | 19000  |
| Ford      | F-150 Lightning  | QS41252           | 2547896      | Carga      | 22000  |
| Toyota    | 4Runner          | 34RF123           | 4587563      | Carga      | 25000  |
| Chevrolet | Corvette         | 4TQWE5            | 2512545      | Particular | 60000  |

## Se agrega menú con Bootstrap 

- se incluye en settings.py dentro de las aplicaciones bootstrap, posteriormente nos dirigimos a la documentación oficial para obtener el codigo del navbar.
- Se crea el archivo navbar.html 

## Permisos:
- para visualizar catalogo y añadir vehiculos: 
~~~    
 class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede visualizar Catálogo de Vehículos"),
            ("Can_add_vehiculo_model", "Puede agregar un vehiculo")
        ]
~~~

## Registro usuarios nuevos:

- Se crea una nueva app llamada usuarios
- proyecto_vehiculos_django/usuarios/views.py:
```
class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            visualizar_permiso = Permission.objects.get(codename='visualizar_catalogo')
            user.user_permissions.add(visualizar_permiso)
            messages.success(request, '¡Registro exitoso!')
            return redirect('index')
        return render(request, self.template_name, {'form': form})
```
- Cada vez que se registra un usuario adquiere el permiso visualizar catalogo.

