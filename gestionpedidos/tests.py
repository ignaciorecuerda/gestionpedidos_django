from django.test import TestCase
from gestionpedidos.models import Cliente, Pedido
from gestionpedidos.views import *
from django.test.client import RequestFactory

class TestsGestionPedidos(TestCase):

	def test_crear_cliente(self):
		Cliente.objects.create(nombre='Test',slug='test',direccion='Pais, ciudad, calle')

	def test_nombre_cliente(self):
		cliente = Cliente.objects.get(name='Test')
		self.assertEqual(cliente.direccion, 'Pais, ciudad, calle')
		print ("direccion correcta")
