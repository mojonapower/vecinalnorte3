from django.db import models

# Create your models here.
class Material_mediomenor(models.Model):
    nombre=models.CharField(max_length=255)
    descripcion=models.CharField(max_length=1000)
    link=models.URLField(max_length=500)

