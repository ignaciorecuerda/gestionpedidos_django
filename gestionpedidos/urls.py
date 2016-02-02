from django.conf.urls import patterns, url
from gestionpedidos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_cliente/$', views.add_cliente, name='add_cliente'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^cliente/(?P<cliente_name>\w+)/add_pedido/$', views.add_pedido, name='add_pedido'),
    url(r'^cliente/(?P<cliente_name_slug>[\w\-]+)/$', views.cliente, name='cliente'),
    url(r'^register/$', views.register, name='register'),
    url(r'^reclama_datos/', views.reclama_datos, name='reclama_datos'),)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )