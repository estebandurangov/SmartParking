from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=100)
    cel = models.CharField(max_length=10)
    correo = models.EmailField()
    
class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=10)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class Celda(models.Model):
    id = models.AutoField(primary_key=True)
    disponibilidad = models.BooleanField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
