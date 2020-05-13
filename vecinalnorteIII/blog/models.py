from django.db import models
from django.utils import timezone


# Create your models here.
class Material_mediomenor(models.Model):
    nombre=models.CharField(max_length=255)
    link=models.URLField(max_length=500)
 

class Material_mediomayor(models.Model):
    nombre=models.CharField(max_length=255)
    link=models.URLField(max_length=500)
    


class Material_medios(models.Model):
    nombre=models.CharField(max_length=255)
    link=models.URLField(max_length=500)
    


class Material_salacuna(models.Model):
    nombre=models.CharField(max_length=255)
    link=models.URLField(max_length=500)
    


class Material_cuentos(models.Model):
    nombre=models.CharField(max_length=255)
    link=models.URLField(max_length=500)
    


