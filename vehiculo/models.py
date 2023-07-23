from django.db import models
from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver


# Modelo de la tabla Vehiculo en la base de datos
class Vehiculo(models.Model):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]
    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]
    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    # Método para retornar el nombre del vehículo
    def __str__(self):
        return self.marca + ' ' + self.modelo

    # Añadir permisos
    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede visualizar el catálogo de vehículos"),
            ("agregar_vehiculo", "Puede agregar un nuevo vehículo"),
        ]
    
    # Método para retornar la categoría del vehículo
    def precio_categoria(self):
        if self.precio <= 10000:
            return 'Bajo'
        elif self.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'

# Signal para añadir el permiso 'visualizar_catalogo' a los nuevos usuarios
@receiver(post_save, sender=User)
def add_permiso_visualizar(sender, instance, created, **kwargs):
    if created:
        permiso = Permission.objects.get(codename='visualizar_catalogo')
        instance.user_permissions.add(permiso)
