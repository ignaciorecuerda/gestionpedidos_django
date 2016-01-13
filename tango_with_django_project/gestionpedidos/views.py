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
    cliente_list = Cliente.objects.all()
    context_dict = {'clientes': cliente_list}

    # Render the response and send it back!
    return render(request, 'gestionpedidos/about.html', context_dict)

def cliente(request, cliente_name_slug):

    context_dict = {}

    try:
        cliente = Cliente.objects.get(slug=cliente_name_slug)
        context_dict['cliente_name'] = cliente.name
        context_dict['cliente_direccion'] = cliente.direccion

        pedidos = Pedido.objects.filter(cliente=cliente)

        context_dict['pedidos'] = pedidos
        context_dict['cliente'] = cliente
    except Cliente.DoesNotExist:
        pass

    return render(request, 'gestionpedidos/pedidos.html', context_dict)

def add_cliente(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = ClienteForm()

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

    registered = False

    if request.method == 'POST':
        
        user_form = UserForm(data=request.POST)
        profile_form = PerfilUsuarioForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():            
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = PerfilUsuarioForm()

    return render(request,
            'gestionpedidos/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

#Devuelve los datos para las graficas
def reclama_datos(request):
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