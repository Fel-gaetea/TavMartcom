from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
]

urlpatterns += [
    path('Cliente/create/', views.ClienteCreate.as_view(), name='Cliente_create'),
    path('Cliente/<int:pk>/update/', views.ClienteUpdate.as_view(), name='Cliente_update'),
    path('Cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='Cliente_delete'),
]

urlpatterns += [
    path('equipamiento/create/', views.equipamientoCreate.as_view(), name='equipamiento_create'),
    path('equipamiento/<int:pk>/update/', views.equipamientoUpdate.as_view(), name='equipamiento_update'),
    path('equipamiento/<int:pk>/delete/', views.equipamientoDelete.as_view(), name='equipamiento_delete'),
]