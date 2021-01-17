from django.db import models

# Create your models here.

class Domicilio(models.Model):
       calle=models.CharField(max_length=255)
       numero=models.IntegerField()
       pais=models.CharField(max_length=255)

       def __str__(self):
              return(f'{self.pais} {self.calle} {self.numero}')

class Persona(models.Model):
       nombre=models.CharField(max_length=255)
       apellido=models.CharField(max_length=255)
       correo=models.CharField(max_length=255)
       domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)

       def __str__(self):
              return(f'{self.nombre}  {self.apellido} {self.domicilio}')

