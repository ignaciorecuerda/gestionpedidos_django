from django.conf.urls import patterns, url
from gestionpedidos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^cliente/(?P<cliente_name_slug>[\w\-]+)/$', views.cliente, name='cliente'),)