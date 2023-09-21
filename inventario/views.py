from django.shortcuts import render,redirect
from inventario.models import Productos
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def listarProductos(req):
    productos = Productos.objects.all() # equivale a un "SELECT * FROM productos"
    contexto = {"productos":productos}
    return render(req,'index.html',contexto)

@login_required
#Eliminar un producto
def eliminarProducto(req,id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('index')

@login_required
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

@login_required       
def crearProducto(req):
    nombre_post = req.POST["nombre"]
    precio_post = req.POST["precio"]
    stock_post = req.POST["stock"]
    producto = Productos(nombre=nombre_post,precio=precio_post,stock=stock_post)
    producto.save() #SI O SI PRECISO EL SAVE , PARA GUARDAR MI PRODUCTO
    return redirect('index')