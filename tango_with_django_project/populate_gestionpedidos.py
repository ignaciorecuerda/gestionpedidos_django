# -- coding: utf-8 -
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from gestionpedidos.models import Cliente, Pedido


def populate():
    carlos_cliente = add_cli('Carlos')

    add_pedido(cli=carlos_cliente,
        title="Altavoces Sony SRS-X99",
        url="http://www.sony.es/electronics/altavoces-inalambricos/srs-x99",
        fechaPedido="3/11/15",
        precio="700 euros")

    add_pedido(cli=carlos_cliente,
        title="Monitor Dell 22 S2216H",
        url="http://www1.euro.dell.com/content/products/productdetails.aspx/dell-s2216h-monitor?c=es&cs=esdhs1&l=es&s=dhs",
        fechaPedido="4/11/15",
        precio="217 euros")

    add_pedido(cli=carlos_cliente,
        title="Ray-ban aviator",
        url="http://www.ray-ban.com/spain/gafas-de-sol/aviator/clv",
        fechaPedido="4/11/15",
        precio="149 euros")

    quique_cliente = add_cli('Quique')

    add_pedido(cli=quique_cliente,
        title="Kawasaki Z800",
        url="http://www.kawasaki.es/es/products",
        fechaPedido="7/11/15",
        precio="8.899 euros")

    add_pedido(cli=quique_cliente,
        title="Mercedes-benz clase C",
        url="http://www.mercedes-benz.es/content/spain/mpc/mpc_spain_website/es/home_mpc/passengercars.flash.html",
        fechaPedido="20/11/15",
        precio="38.000 euros")

    add_pedido(cli=quique_cliente,
        title="Mercedes-benz clase E",
        url="http://www.mercedes-benz.es/content/spain/mpc/mpc_spain_website/es/home_mpc/passengercars.flash.html",
        fechaPedido="22/11/15",
        precio="51.900 euros")

    rocio_cliente = add_cli('Rocio')

    add_pedido(cli=rocio_cliente,
        title="Televisor LED K32DLM3H 32",
        url="http://www.carrefour.es/televisor-led-td-systems-k32dlm3h-32/2001690052/p",
        fechaPedido="25/11/15",
        precio="199 euros")

    add_pedido(cli=rocio_cliente,
        title="Carro niño 3 piezas",
        url="http://www.carrefour.es/coche-de-3-piezas-asalvo-baby-trio-miami-2015/2001120345/p",
        fechaPedido="25/11/15",
        precio="279 euros")

    # Print out what we have added to the user.
    for c in Cliente.objects.all():
        for p in Pedido.objects.filter(cliente=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_pedido(cli, title, url, fechaPedido, precio, views=0):
    p = Pedido.objects.get_or_create(cliente=cli, title=title)[0]
    p.url=url
    p.views=views
    p.fechaPedido=fechaPedido
    p.precio=precio
    p.save()
    return p

def add_cli(name):
    c = Cliente.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting gestionpedidos population script..."
    populate()