from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(max_length= 12, unique = True)
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    email = models.CharField(max_length= 30)
