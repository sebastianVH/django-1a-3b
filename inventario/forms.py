#aqui vamos a crear nuestros forms para hacer todo mas EFICIENTE en el manejo de Django
#? Ventaja: Velocidad de procesamiento de campos necesarios, al igual que el uso de VALIDACIONES propias que tiene el form
#! Desventaja: Forms requieren que los estilos les sean dados DESDE CSS. Esto debido a que NO TENDREMOS ACCESO DESDE HTML AL ELEMENTO.

#Django se encarga de crear el HTML necesario que se renderizado del lado del cliente
from django import forms
from .models import Productos

class FormProducto(forms.ModelForm):

    class Meta:
        error = "Errors Found in the Form"
        model = Productos
        fields = '__all__'
        
        
        