from django.forms import ModelForm

from personas.models import Domicilio


class Formdomicilio(ModelForm):#Creamos una clase para administrar mejor el form y pode editar los datos a nuestro gusto
    class Meta:
        model=Domicilio#nombre del modelo de donde vamos a recibir los datos o enviar
        fields='__all__'#indicamos que vamos a utilizar todos los archivos
       # widgets={#es un dicionarrio para el correo para indicar si no esta bien escrito se puede buscar la informacion para dale
        #    #estilo buscar en la documentacion
         #   'email': EmailInput(attrs={'type':'email'})#hacemos el diccionaro y utlizamos la importacion del metodo aque utilizamos
          #  #codigo html en attrs en adelente

        #}
