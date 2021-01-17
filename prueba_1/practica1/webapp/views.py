from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Bienvenido(request):
    return HttpResponse('Bienvenido')
def Despedida(request):
    return HttpResponse('Adios')
def Contacto(request):
    return HttpResponse('Ricardo Altamirano Sanchez '
                        'ricardo@gmail.com'
                        '5539709404')