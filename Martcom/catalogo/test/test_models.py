from django.test import TestCase
from  .models import Cliente, equipamiento,Servicios

class ClienteTestCase(TestCase):

    def setUpTestData(self):
        Cliente.objects.create(nom='Felipe')

    def setUpTestData(self):
        Cliente.objects.create(apell='Gaete')

class equipamientoTestCase(TestCase):

    def setUpTestData(self):
        equipamiento.objects.create(name='Medidor de Potencia')

class ServiciosTestCase(TestCase):

    def setUpTestData(self):
        Servicios.objects.create(title='Electricidad')    
 