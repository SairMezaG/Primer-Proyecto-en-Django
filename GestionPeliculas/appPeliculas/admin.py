from django.contrib import admin
from appPeliculas.models import Genero,Pelicula
# Register your models here.

#  Esto me permite visualizar en el administrador de Django los modelos generados 
# para su administración.
admin.site.register(Genero)
admin.site.register(Pelicula)
