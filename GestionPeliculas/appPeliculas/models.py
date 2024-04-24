from django.db import models

# Create your models here.

class Genero(models.Model):
    genNombre = models.CharField(max_length=50, unique=True)


class Pelicula(models.Model):
    codigo= models.CharField(max_length=9)
    titulo= models.CharField(max_length=50)
    protagonista= models.CharField(max_length=50)
    duracion= models.IntegerField()
    resumen= models.CharField(max_length=2000)
    foto = models.ImageField(upload_to="fotos/", null=True, blank=True)
    genero= models.ForeignKey(Genero, on_delete=models.PROTECT)   
