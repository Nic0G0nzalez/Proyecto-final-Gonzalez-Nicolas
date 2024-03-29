from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
#__________________________Inicio
def inicio(request):
    return render(request, "Dietetica/index.html")

#__________________________Vendedores
@login_required
def vendedores(request):
    return render(request, "Dietetica/Vendedores.html")

class VendedoresList(LoginRequiredMixin, ListView):
    model= Vendedores

class VendedoresCreate(LoginRequiredMixin, CreateView):
    model= Vendedores
    fields=["nombre", "apellido", "email","DNI"]
    success_url= reverse_lazy("Vendedores")

class VendedoresUpdate(LoginRequiredMixin, UpdateView):
    model= Vendedores
    fields=["nombre", "apellido", "email","DNI"]
    success_url= reverse_lazy("Vendedores")

class VendedoresDelete(LoginRequiredMixin, DeleteView):
    model= Vendedores
    success_url= reverse_lazy("Vendedores")



#__________________________Clientes
@login_required
def clientes(request):
    return render(request, "Dietetica/Clientes.html")

class ClientesList(LoginRequiredMixin, ListView):
    model= Clientes

class ClientesCreate(LoginRequiredMixin, CreateView):
    model= Clientes
    fields=["nombre", "apellido", "email","DNI"]
    success_url= reverse_lazy("Clientes")

class ClientesUpdate(LoginRequiredMixin, UpdateView):
    model= Clientes
    fields=["nombre", "apellido", "email","DNI"]
    success_url= reverse_lazy("Clientes")

class ClientesDelete(LoginRequiredMixin, DeleteView):
    model= Clientes
    success_url= reverse_lazy("Clientes")


#__________________________Productos
@login_required
def productos(request):
    return render(request, "Dietetica/Productos.html")

class ProductosList(LoginRequiredMixin, ListView):
    model= Productos

class ProductosCreate(LoginRequiredMixin, CreateView):
    model= Productos
    fields=["nombre", "cantidad_en_gramos", "precio_en_pesos"]
    success_url= reverse_lazy("Productos")

class ProductosUpdate(LoginRequiredMixin, UpdateView):
    model= Productos
    fields=["nombre", "cantidad_en_gramos", "precio_en_pesos"]
    success_url= reverse_lazy("Productos")

class ProductosDelete(LoginRequiredMixin, DeleteView):
    model= Productos
    success_url= reverse_lazy("Productos")

@login_required
def buscarProductos(request):
    return render(request, "Dietetica/buscar_productos.html")

@login_required
def encontrarProductos(request):
    if request.GET.get("buscar"):
        patron = request.GET["buscar"]
        productos = Productos.objects.filter(nombre__icontains=patron)
        return render(request, "Dietetica/productos_list.html", {"productos_list": productos})
    
    return redirect(reverse_lazy("buscar_productos"))

#__________________________Productos al por mayor
@login_required
def productos_por_mayor(request):
    return render(request, "Dietetica/Productos_por_mayor.html")

class ProductosPorMayorList(LoginRequiredMixin, ListView):
    model= ProductosPorMayor

class ProductosPorMayorCreate(LoginRequiredMixin, CreateView):
    model= ProductosPorMayor
    fields=["nombre", "cantidad_en_kg", "precio_en_pesos"]
    success_url= reverse_lazy("Productos_por_mayor")

class ProductosPorMayorUpdate(LoginRequiredMixin, UpdateView):
    model= ProductosPorMayor
    fields=["nombre", "cantidad_en_kg", "precio_en_pesos"]
    success_url= reverse_lazy("Productos_por_mayor")

class ProductosPorMayorDelete(LoginRequiredMixin, DeleteView):
    model= ProductosPorMayor
    success_url= reverse_lazy("Productos_por_mayor")


#__________________________Login, logout, registro, modificacion de usuario y agregar avatar
def login_request(request):
    if request.method == "POST":
        usuario= request.POST['username']
        clave= request.POST['password']
        user= authenticate(request, username= usuario, password= clave)
        if user is not None:
            login(request, user)
            try:
                avatar= Avatar.objects.get(user= request.user.id).imagen.url
            except:
                avatar= "/media/avatares/default.png"
            finally:
                request.session["avatar"]= avatar
            return render(request, "Dietetica/index.html")
        else:
            return redirect(reverse_lazy('login'))
    
    else:
        miForm= AuthenticationForm()
    return render (request, "Dietetica/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm= RegistroForm(request.POST)
        if miForm.is_valid():
            usuario= miForm.cleaned_data.get("username")
            miForm.save()
            return redirect (reverse_lazy('inicio'))
            
    else:
        miForm= RegistroForm()
    return render (request, "Dietetica/registro.html", {"form": miForm})

@login_required
def EditProfile(request):
    usuario= request.user
    if request.method == "POST":
        miForm= UserEditForm(request.POST)
        if miForm.is_valid():
            user=User.objects.get(username=usuario)
            user.email= miForm.cleaned_data.get("email")
            user.first_name= miForm.cleaned_data.get("first_name")
            user.last_name=miForm.cleaned_data.get("last_name")
            user.save()
            return redirect (reverse_lazy('inicio'))
            
    else:
        miForm= UserEditForm(instance=usuario)
    return render (request, "Dietetica/editar_perfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name="Dietetica/cambiar_clave.html"
    success_url= reverse_lazy("inicio")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #_____________________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #______________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('inicio'))
    else: 
        miForm = AvatarForm()

    return render(request, "Dietetica/agregar_avatar.html", {"form": miForm} )         

#__________________________Acerca de mi
def acerca_de_mi(request):
    return render(request, "Dietetica/acerca_de_mi.html")




