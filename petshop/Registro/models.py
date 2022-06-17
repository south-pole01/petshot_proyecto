from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    stock = models.IntegerField()
    comentario = models.CharField(max_length=50)
    precio = models.IntegerField()


    def __str__(self):
        return self.nombre
