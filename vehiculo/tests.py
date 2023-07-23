from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Vehiculo

# Create your tests here.

# Test para el modelo Vehiculo
class VehiculoModelTest(TestCase):
    def setUp(self):
        self.vehiculo = Vehiculo.objects.create(
            marca='Fiat',
            modelo='500',
            serial_carroceria='12345',
            serial_motor='54321',
            categoria='Particular',
            precio=20000,
        )
    # Test para verificar que el modelo Vehiculo se crea correctamente
    def test_vehiculo_creation(self):
        self.assertEqual(self.vehiculo.marca, 'Fiat')
        self.assertEqual(self.vehiculo.modelo, '500')
        self.assertEqual(self.vehiculo.serial_carroceria, '12345')
        self.assertEqual(self.vehiculo.serial_motor, '54321')
        self.assertEqual(self.vehiculo.categoria, 'Particular')
        self.assertEqual(self.vehiculo.precio, 20000)

    # Test para verificar que el método precio_categoria funciona correctamente
    def test_precio_categoria(self):
        self.assertEqual(self.vehiculo.precio_categoria(), 'Medio')

# Test para las vistas de Vehiculo
class VehiculoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@email.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
    
    # Test para verificar que la vista vehiculo_list funciona correctamente
    def test_vehiculo_list_view(self):
        response = self.client.get(reverse('vehiculo:vehiculo_list'))
        self.assertEqual(response.status_code, 200)
