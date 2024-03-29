from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#____________________________ Modelo cliente
class Clientes(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField(max_length=40)
    DNI= models.IntegerField()
    

    def __str__(self):
        return f"Cliente {self.nombre} {self.apellido}"

#____________________________ Modelo vendedor
class Vendedores(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField(max_length=40)
    DNI= models.IntegerField()

    def __str__(self):
        return f"Vendedor {self.nombre} {self.apellido}"

#____________________________ Modelo producto
class Productos(models.Model):
    nombre= models.CharField(max_length=40)
    cantidad_en_gramos= models.IntegerField()
    precio_en_pesos= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} por {self.cantidad_en_gramos}"

#____________________________ Modelo producto por mayor
class ProductosPorMayor(models.Model):
    nombre= models.CharField(max_length=40)
    cantidad_en_kg= models.IntegerField()
    precio_en_pesos= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} por {self.cantidad_en_kg}"

#____________________________ Modelo avatar
class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatares")
    user= models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"

