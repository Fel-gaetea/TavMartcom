from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.nosotros, name='nosotros'),
    path('', views.servicios, name='servicios'),
    path('', views.contacto, name='contacto'),
]

urlpatterns += [
    path('Cliente/create/', views.AuthorCreate.as_view(), name='Cliente_create'),
    path('Cliente/<int:pk>/update/', views.AuthorUpdate.as_view(), name='Cliente_update'),
    path('Cliente/<int:pk>/delete/', views.AuthorDelete.as_view(), name='Cliente_delete'),
]

urlpatterns += [
    path('equipamiento/create/', views.AuthorCreate.as_view(), name='equipamiento_create'),
    path('equipamiento/<int:pk>/update/', views.AuthorUpdate.as_view(), name='equipamiento_update'),
    path('equipamiento/<int:pk>/delete/', views.AuthorDelete.as_view(), name='equipamiento_delete'),
]