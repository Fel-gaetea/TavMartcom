from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.nosotros, name='nosotros'),
    path('', views.servicios, name='servicios'),
    path('', views.contacto, name='contacto'),
]