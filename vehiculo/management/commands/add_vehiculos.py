from django.core.management.base import BaseCommand
from vehiculo.models import Vehiculo

class Command(BaseCommand):
    help = 'Agrega vehículos a la base de datos'

    def handle(self, *args, **options):
        vehiculos = [
            {
                'marca': 'Fiat', 
                'modelo': 'Punto', 
                'serial_carroceria': '254AADD', 
                'serial_motor': '4521475', 
                'categoria': 'Particular', 
                'precio': 9200
            },
            {
                'marca': 'Fiat', 
                'modelo': 'Furgoneta Ducato', 
                'serial_carroceria': '25ED235', 
                'serial_motor': '8554122', 
                'categoria': 'Transporte', 
                'precio': 19000
            },
            {
                'marca': 'Ford', 
                'modelo': 'F-150 Lightning', 
                'serial_carroceria': 'QS41252', 
                'serial_motor': '2547896', 
                'categoria': 'Carga', 
                'precio': 22000
            },
            {
                'marca': 'Toyota', 
                'modelo': '4Runner', 
                'serial_carroceria': '34RF123', 
                'serial_motor': '4587563', 
                'categoria': 'Carga', 
                'precio': 25000
            },
            {
                'marca': 'Chevrolet', 
                'modelo': 'Corvette', 
                'serial_carroceria': '4TQWE5', 
                'serial_motor': '2512545', 
                'categoria': 'Particular', 
                'precio': 60000
            },
        ]

        for vehiculo in vehiculos:
            Vehiculo.objects.create(**vehiculo)

        self.stdout.write(self.style.SUCCESS('Los vehículos han sido agregados exitosamente.'))
