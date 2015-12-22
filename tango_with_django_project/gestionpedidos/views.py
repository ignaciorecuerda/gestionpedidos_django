from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import Cliente, Pedido
from gestionpedidos.forms import ClienteForm, PedidoForm
from django.contrib.auth.decorators import login_required

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
        # Can we find a cliente name slug with the given name?
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

def add_cliente(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ClienteForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'gestionpedidos/add_cliente.html', {'form': form})


def add_pedido(request, cliente_name):

    try:
        cat = Cliente.objects.get(name=cliente_name)
    except Cliente.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            if cat:
                pedido = form.save(commit=False)
                pedido.cliente = cat
                pedido.views = 0
                pedido.save()
                # probably better to use a redirect here.
                return cliente(request, cliente_name)
        else:
            print form.errors
    else:
        form = PedidoForm()

    context_dict = {'form':form, 'cliente': cat}

    return render(request, 'gestionpedidos/add_pedido.html', context_dict)


@login_required
def restricted(request):
    return render(request, 'gestionpedidos/restricted.html')

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/gestionpedidos/')
