from django.test import TestCase
from gestionpedidos.models import Cliente, Pedido
from gestionpedidos.views import *
from django.test.client import RequestFactory

class TestsGestionPedidos(TestCase):
	def test_nombre_cliente(self):
		cliente = Cliente.objects.get(name="Quique")
		self.assertEqual(cliente.direccion, 'Spain, Granada, recogidas')
		print ("direccion correcta")
