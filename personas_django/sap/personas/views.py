from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from personas.form import Formpersona
from personas.models import Persona, Domicilio


def Equipo_info(request,id):
    # equipo=Persona.objects.get(pk=id)#primero metodo
    equipo=get_object_or_404(Persona,pk=id)#segundo metodo este te envia ala pagina de error
    return render(request,'Equipo/equipo.html', {'equipo' : equipo})

#Formpersona=modelform_factory(Persona,exclude=[]) #esto es para obtener la clase de formulario y despues usarlo en la etiqueta html


def Nueva_persona(request):
    if request.method=='POST':#vemos si la peticion ess de tipo post o get
        formapersona=Formpersona(request.POST)#Creamos una objeto que cuando con toda la informacion que nos esta enviando
        if formapersona.is_valid():#vemos si es valido el objeto si es una peticion post
              formapersona.save()#se guarda el objeto en la base de datos
              return redirect('inicio')
          #nota en la plantilla html debemos poner la funcion post en minuscula para que nos agarre la peticion y aquie en mayuasculas
         #en python

    else:
     formapersona=Formpersona()
    return render(request,'Equipo/nueva_persona.html',{'formapersona':formapersona})



def Editar_persona(request,id):#para la funcion es igual que crear un nuevo registro pero se debe poner el id de la persona a editar
    persona =get_object_or_404(Persona, pk=id)  # segundo metodo este te envia ala pagina de error
    if request.method=='POST':#vemos si la peticion ess de tipo post o get
        formapersona=Formpersona(request.POST,instance=persona)#Creamos una objeto que cuando con toda la informacion que nos esta enviando debemos poner instance parq que sea una acutalizacion y no un nuevo registro
        if formapersona.is_valid():#vemos si es valido el objeto si es una peticion post
              formapersona.save()#se guarda el objeto en la base de datos
              return redirect('inicio')
          #nota en la plantilla html debemos poner la funcion post en minuscula para que nos agarre la peticion y aqui en mayuasculas
         #en python

    else:
            formapersona=Formpersona(instance=persona)
    return render(request,'Equipo/editar_persona.html',{'formapersona':formapersona})

def Eliminar_persona(request,id):
    persona=get_object_or_404(Persona,pk=id)#no da el usuario en la base de datos
    if persona:
        persona.delete()
        return redirect('inicio')

def Domicilio_info(request):
    no_domicilios=Domicilio.objects.count
    domicilio=Domicilio.objects.all
    return render(request,'Domicilio/inicio_domicilio.html',{'no_domicilios':no_domicilios,'domicilio':domicilio})
def Domicilio_mas(request,id):
    domicilio=get_object_or_404(Domicilio,pk=id)
    return render(request,'Domicilio/Domicilio_mas.html',{'domicilio':domicilio})