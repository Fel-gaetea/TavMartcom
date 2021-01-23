from django.db import models
from django.urls import reverse
import uuid #requerido para id partner

# Create your models here.
class partner(models.Model):
    name=models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class equipamiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name=models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse ('equipamiento-detail',args=[str(self.id)])


    def __str__(self):
        return self.name


class Cliente(models.Model):
    rut = models.CharField(primary_key=True,max_length=10)
    nom = models.CharField(max_length=100)
    apell = models.CharField(max_length=100)
    fono = models.CharField(max_length=9)
    direc = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)

    def str(self):

        return self.rut

class Meta:

    ordering = ['apell', 'nom']

def __str__(self):
    return f'{self.nom}, {self.apell}' 



class Servicios(models.Model):
    title = models.CharField(max_length=200)
    descrip = models.CharField(max_length=1000)
    imag = models.ImageField (upload_to='services')

    def str(self):

        return self.title