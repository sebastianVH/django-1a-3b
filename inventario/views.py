from django.shortcuts import render,redirect,get_object_or_404
from inventario.models import Productos,Categorias
from django.contrib.auth.decorators import login_required
from .forms import FormProducto
# Create your views here.


def listarProductos(req):
    productos = Productos.objects.all() # equivale a un "SELECT * FROM productos"
    categorias = Categorias.objects.all() #equivale a un "SELECT * FROM categorias"
    formulario = FormProducto()
    #rendericemos en el CONTEXTO 
    contexto = {"productos":productos,"categorias":categorias,"formulario":formulario}
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
    # producto = Productos.objects.get(id=id)
    # lista_categorias = Categorias.objects.all()
    producto = get_object_or_404(Productos,id=id)
    
    if req.method == "GET":
        formulario = FormProducto(instance=producto)
        contexto = {"producto":producto,"formulario":formulario}
        return render(req,'editar.html',contexto)
    
    elif req.method == "POST":
        #capturar los datos del post
        # nombre_nuevo = req.POST["nombre"]
        # precio_nuevo = req.POST["precio"]
        # stock_nuevo = req.POST["stock"]
        # id_categoria_nueva = req.POST["categoria"]
        # categoria_nueva = Categorias.objects.get(id=id_categoria_nueva) 
        # producto.nombre = nombre_nuevo
        # producto.precio = precio_nuevo
        # producto.stock = stock_nuevo
        # producto.categoria_fk = categoria_nueva #! GUARDAMOS INSTANCIAS!!!! (creacion de un objeto)
        # #necesito SI O SI VOLVER A GUARDAR ESE PRODUCTO
        # producto.save()
        formulario = FormProducto(req.POST,instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')

@login_required       
def crearProducto(req):
    # nombre_post = req.POST["nombre"]
    # precio_post = req.POST["precio"]
    # stock_post = req.POST["stock"]
    # categoria_id = req.POST["categoria"]
    # categoria_instance = Categorias.objects.get(id=categoria_id)
    # producto = Productos(nombre=nombre_post,precio=precio_post,stock=stock_post,categoria_fk=categoria_instance)
    # producto.save() #SI O SI PRECISO EL SAVE , PARA GUARDAR MI PRODUCTO
    #? Form de creacion de producto:
    form_producto = FormProducto(req.POST)
    if form_producto.is_valid():
        form_producto.save()
        return redirect('index')