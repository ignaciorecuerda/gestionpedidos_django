from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import Cliente, Pedido
from gestionpedidos.forms import ClienteForm, PedidoForm, UserForm, PerfilUsuarioForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def index(request):
    cliente_list = Cliente.objects.all()
    context_dict = {'clientes': cliente_list}
    
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
        context_dict['cliente_direccion'] = cliente.direccion

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


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = PerfilUsuarioForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = PerfilUsuarioForm()

    # Render the template depending on the context.
    return render(request,
            'gestionpedidos/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

#Devuelve los datos para las graficas
def reclama_datos(request):
    print '------> ENTRA EN reclama_datos!!!!!!'
    listaClientes = Cliente.objects.all()    
    context_dict = {'clientes': listaClientes}

    datosJson=[]

    #numero de pedidos de cada cliente
    for cliente in listaClientes:  
        #meto el nombre del cliente
        datosJson.append(cliente.name)

        pedidos = Pedido.objects.filter(cliente=cliente)
        #meto el numero de pedidos del cliente
        datosJson.append(pedidos.count())

    return JsonResponse(datosJson, safe=False)