from django.db import models

# Create your models here.
class Categorias(models.Model):
    """ correspondera a la clase Categorias: 1 producto tendra una sola categoria, pero una categoria, puede estas presente en muchos productos
        Existira una relacion de 1 a M
    """
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name
    
    class Meta:
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
        
class Productos(models.Model):
    """ Modelo para la creacion de objetos de Productos """
    nombre = models.CharField(max_length=30, null=False)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    categoria_fk = models.ForeignKey(Categorias,on_delete=models.CASCADE,null=True,default=1) #Esta sera la FK que nos relaciona con la clase de Categorias
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
