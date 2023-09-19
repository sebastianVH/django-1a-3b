from django.db import models

# Create your models here.
class Productos(models.Model):
    """ Modelo para la creacion de objetos de Productos """
    nombre = models.CharField(max_length=30, null=False)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    