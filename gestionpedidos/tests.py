from django.test import TestCase
from gestionpedidos.models import Cliente, Pedido
from gestionpedidos.views import *
from django.test.client import RequestFactory

class TestsGestionPedidos(TestCase):

	#Test para clientes
	def setUp(self):
		Cliente.objects.create(name='Test',slug='test',direccion='Pais, ciudad, calle')

	def test_cliente(self):
		cliente = Cliente.objects.get(name='Test')
		self.assertEqual(cliente.name, 'Test')
		self.assertEqual(cliente.slug, 'test')
		self.assertEqual(cliente.direccion, 'Pais, ciudad, calle')
		print ("direccion correcta")

	#test para pedidos
	def setUp(self):
		test = Cliente(name='TestTapas',slug='testTapas',direccion='Pais, ciudad, calle')
		Pedido.objects.create(cliente='test', title='TestPedido', url="www.test.es", views=1, fechaPedido='02/02/16', precio='1 euro')

	def test_pedido(self):
		pedido = Pedido.objects.get(title='TestPedido')
		self.assertEqual(pedido.title, 'TestPedido')
		self.assertEqual(pedido.url, 'www.test.es')
		self.assertEqual(pedido.views, 1)
		self.assertEqual(pedido.fechaPedido, '02/02/16')
		self.assertEqual(pedido.precio, '1 euro')