"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personas.views import Equipo_info, Nueva_persona, Editar_persona, Eliminar_persona, Domicilio_info, Domicilio_mas
from webapp.views import  Inicio_main

# Despedida,Contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('Bienvenido/',Bienvenido),
    path('',Inicio_main,name='inicio'),#usamo name para podenerle un alias y se mas facil su uso
   # path('Despedida/',Despedida),
    #path('Contacto/',Contacto),
    path('Informacion_Persona/<int:id>',Equipo_info),
    path('nueva_persona/',Nueva_persona),
    path('Editar_persona/<int:id>', Editar_persona),
    path('Eliminar_persona/<int:id>', Eliminar_persona),
    path('Inicio_domicilio/',Domicilio_info,name='inicio_domicilio'),
    path('Domiciio_mas/',Domicilio_mas),

]
