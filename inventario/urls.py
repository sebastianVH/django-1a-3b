from django.urls import path
from inventario.views import listarProductos,eliminarProducto,editarProducto

urlpatterns = [
    path('',listarProductos,name="index"),
    path('eliminar/<id>',eliminarProducto,name="eliminar"),
    path('editar/<id>',editarProducto,name="editar"),
]
