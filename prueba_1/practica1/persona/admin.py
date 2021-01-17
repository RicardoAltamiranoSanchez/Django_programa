from django.contrib import admin

# Register your models here.
from persona.models import Domicilio, Persona

admin.site.register(Persona)
admin.site.register(Domicilio)