from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def Inicio_main(request):
    no_personas =Persona.objects.count()
    persona=Persona.objects.order_by('id')#Obtenemos toda la informacion de la base de datos con el objetc manager
    return render(request,'Inicio_principal.html',{'no_personas': no_personas, 'persona': persona})





























































#mensaje={'msg1':'mensaje 1', 'msg2':'mensaje 2'}
# de pedimos la base de datos cuantos registros hay obejtc es funcion de para pedir un
# dela base de datos object objeto manager
# def Despedida(request):
#   return HttpResponse('Adios a todos mueran')
# def Contacto(request):
#   return HttpResponse('Nombre Ricardo Altamirano Sanchez'
#         'Correo ricardohh9385@gmail.com'
#        'Telefono 5539709404')

