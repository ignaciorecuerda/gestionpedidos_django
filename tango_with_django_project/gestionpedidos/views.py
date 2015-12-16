from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import Cliente, Pedido

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    cliente_list = Cliente.objects.all()
    context_dict = {'clientes': cliente_list}

    # Render the response and send it back!
    return render(request, 'gestionpedidos/index.html', context_dict)

def about(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    cliente_list = Cliente.objects.all()
    context_dict = {'clientes': cliente_list}

    # Render the response and send it back!
    return render(request, 'gestionpedidos/about.html', context_dict)

def cliente(request, cliente_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        cliente = Cliente.objects.get(slug=cliente_name_slug)
        context_dict['cliente_name'] = cliente.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pedidos = Pedido.objects.filter(cliente=cliente)

        # Adds our results list to the template context under name pedidos.
        context_dict['pedidos'] = pedidos
        # We also add the cliente object from the database to the context dictionary.
        # We'll use this in the template to verify that the cliente exists.
        context_dict['cliente'] = cliente
    except Cliente.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'gestionpedidos/pedidos.html', context_dict)

