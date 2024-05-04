from django.shortcuts import render, redirect
from django.db import Error
from appPeliculas.models import Genero, Pelicula
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt





""" def vistaAgregarGenero(request):
     return render(request, "agregarGenero.html")
 """

def inicio(request):
    return render(request, "inicioDeSesion.html")

def agregarGenero(request):
    mensaje = ''  
    if request.method == 'POST':
        try:
            nombre = request.POST['txtGenero']
            genero = Genero.objects.create(nombre=nombre)
            mensaje = 'Género agregado correctamente'
        except Exception as e:
            mensaje = str(e)
    
    return render(request, 'agregarGenero.html', {'mensaje': mensaje})




""" def vistaAgregarPelicula(request):
    generos= Genero.objects.all()
    retorno= {"generos": generos}
    return render(request, "agregarPelicula.html", retorno)
 """





def agregarPelicula(request):
    mensaje = ""

    if request.method == 'POST':
        try:
            codigo = request.POST['txtCodigo']
            titulo = request.POST['txtTitulo']
            protagonista = request.POST['txtProtagonista']
            duracion = int(request.POST['txtDuracion'])
            resumen = request.POST['txtResumen']
            foto = request.FILES['foto']  
            idGenero = int(request.POST['idGenero'])  
            genero = Genero.objects.get(pk=idGenero)
            


            # Para guadar la nueva pelicula (pelicula.save() es reemplazado por: pelicula = Pelicula.objects.create )
            pelicula = Pelicula.objects.create(
                codigo=codigo,
                titulo=titulo,
                protagonista=protagonista,
                duracion=duracion,
                resumen=resumen,
                foto=foto,
                genero=genero
            )
            
            mensaje = "Pelicula agregada correctamente"
        except Exception as e:
            mensaje = str(e)
            pelicula = None

    # Obtener todos los géneros para pasarlos al formulario
    generos = Genero.objects.all()
    retorno = {"mensaje": mensaje, "generos": generos}
    return render(request, 'agregarPelicula.html', retorno) 


    

def listarPeliculas(request):
    peliculas = Pelicula.objects.all()
    retorno = {"peliculas": peliculas}
    return render(request, 'listarPeliculas.html', retorno)
















