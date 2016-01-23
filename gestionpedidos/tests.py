from django.test import TestCase
from gestionpedidos.models import Cliente, Pedido
from django.test.client import RequestFactory

class TestsGestionPedidos(TestCase):
	def test_nombre_cliente(self):
		cliente = Cliente.objects.get(slug="Carlos")
		self.assertEqual(cliente.direccion, 'Spain, Granada, Calle Gran Vía de Colón')
		print ("direccion correcta")
