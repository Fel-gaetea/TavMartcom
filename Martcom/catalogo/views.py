from django.shortcuts import render
from . models import Cliente, partner, equipamiento, Servicios


# Create your views here.



def index(request):

    num_clientes = Cliente.objects.all().count()

    num_partner = partner.objects.all().count()
    
    num_equipamiento = equipamiento.objects.all().count()

    num_servicio=Servicios.objects.all().count()

    return render(

        request,

        'index.html',

        context={'num_clientes': num_clientes, 'num_partner': num_partner, 

        'num_equipamiento': num_equipamiento, 'num_servicios': num_servicio},

    )