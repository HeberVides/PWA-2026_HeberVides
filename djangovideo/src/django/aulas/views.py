#from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.

def hello(request):
    return HttpResponse("Hola mundo")

def bye(request):
    return HttpResponse("chau")

def edad(request, anios, futuro):
    incremento = futuro - date.today().year
    cumplira = anios + incremento
    mensaje="en el año %d cumpliras %d años"%(futuro, cumplira)
    return HttpResponse(mensaje)