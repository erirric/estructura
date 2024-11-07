from django.db import models
from django.db.models import Model

# Create your models here.
generos=[("M", "Masculino"),
         ("F", "Femenino")]
class Usuario(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    cedula = models.CharField(verbose_name="Cedula", max_length=10)
    apellido = models.CharField(verbose_name="Apellido", max_length=50)
    email = models.EmailField(verbose_name="Email")
    estado=models.CharField(default="Espera",max_length=10)
    genero = models.CharField(verbose_name="Genero" ,max_length=1, choices=generos)
    ticket = models.IntegerField(default=1)
    def __str__(self):
           return f"{self.nombre} {self.apellido} - {self.email} - {self.ticket}"
class Archivo(models.Model):
    archivo=models.FileField(verbose_name="Archivo",upload_to='archivos/')

