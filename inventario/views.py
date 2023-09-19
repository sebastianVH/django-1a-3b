from django.shortcuts import render,redirect,HttpResponse
from inventario.models import Productos

# Create your views here.
def listarProductos(req):
    productos = Productos.objects.all() # equivale a un "SELECT * FROM productos"
    contexto = {"productos":productos}
    return render(req,'index.html',contexto)

#Eliminar un producto
def eliminarProducto(req,id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('index')

#Usaremos la funcion para RECIBIR el producto a editar y tambien GUARDAR el producto editado
def editarProducto(req,id):
    producto = Productos.objects.get(id=id)
    
    if req.method == "GET":
        contexto = {"producto":producto}
        return render(req,'editar.html',contexto)
    
    elif req.method == "POST":
        #capturar los datos del post
        nombre_nuevo = req.POST["nombre"]
        precio_nuevo = req.POST["precio"]
        stock_nuevo = req.POST["stock"]
        producto.nombre = nombre_nuevo
        producto.precio = precio_nuevo
        producto.stock = stock_nuevo
        #necesito SI O SI VOLVER A GUARDAR ESE PRODUCTO
        producto.save()
        return redirect('index')
        
    