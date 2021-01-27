from django.shortcuts import render
from . models import Cliente, partner, Servicios, equipamiento
from django.views.generic.edit import CreateView, UpdateView, DeleteView #CRUD de django
from django.urls import reverse_lazy #nos permite redireccionar la informacion de la clase 
from django.views import generic


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

    num_servicios=Servicios.objects.all().count()
    
    return render(

        request,

        'servicios.html',

        context={ 'num_servicios': num_servicios},
    )

def contacto(request):

    num_clientes = Cliente.objects.all().count()
    
    return render(

        request,

        'contacto.html',

        context={ 'num_clientes': num_clientes},
    )


#CRUD cliente
class ClienteCreate(CreateView):
    model=Cliente
    fields='__all__'

class ClienteUpdate(UpdateView):
    model=Cliente
    fields=['rut','nom','apell','fono','direc','email']

class ClienteDelete(DeleteView):
    model=Cliente
    success_url=reverse_lazy('Cliente')

class ClienteDetailView(generic.DetailView):

    """Generic class-based detail view for an author."""

    model = Cliente


#CRUD equipamiento
class equipamientoCreate(CreateView):
    model=equipamiento
    fields='__all__'

class equipamientoUpdate(UpdateView):
    model=equipamiento
    fields=['id','name']

class equipamientoDelete(DeleteView):
    model=equipamiento
    success_url=reverse_lazy('equipamiento')

#CRUD partner
class partnerCreate(CreateView):
    model=partner
    fields='__all__'

class partnerUpdate(UpdateView):
    model=partner
    fields=['name','img']

class partnerDelete(DeleteView):
    model=partner
    success_url=reverse_lazy('partner')

#CRUD servcios

class ServiciosCreate(CreateView):
    model=Servicios
    fields='__all__'

class ServiciosUpdate(UpdateView):
    model=Servicios
    fields=['title','descrip','imag']

class ServiciosDelete(DeleteView):
    model=Servicios
    success_url=reverse_lazy('Servicios')
