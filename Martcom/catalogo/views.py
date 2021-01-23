from django.shortcuts import render
from . models import Cliente, partner, equipamiento, Servicios


# Create your views here.



def index(request):
    
    num_equipamiento = equipamiento.objects.all().count()

    return render(

        request,

        'index.html',

         context={ 'num_equipamiento': num_equipamiento},
    )

    def nosotros(request):
    
    return render(
        request,
        'nosotros.html',
    )

    def servicios(request):

    num_servicio=Servicios.objects.all().count()
    
    return render(

        request,

        'servicios.html',

        context={ 'num_servicios': num_serviciosr},
    )

    def contacto(request):

    num_clientes = Cliente.objects.all().count()
    
    return render(

        request,

        'contacto.html',

        context={ 'num_clientes': num_clientes},
    )