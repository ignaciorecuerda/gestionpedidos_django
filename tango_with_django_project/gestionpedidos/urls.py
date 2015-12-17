from django.conf.urls import patterns, url
from gestionpedidos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_cliente/$', views.add_cliente, name='add_cliente'),
    url(r'^cliente/(?P<cliente_name_url>\w+)/add_pedido/$', views.add_pedido, name='add_pedido'),
    url(r'^cliente/(?P<cliente_name_slug>[\w\-]+)/$', views.cliente, name='cliente'),)