from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from .views import CambiarClave

urlpatterns = [
#________________________Inicio
    path('', inicio, name="inicio"),

#________________________Vendedores
    path('Vendedores/', VendedoresList.as_view(), name="Vendedores"),
    path('vendedores_create/', VendedoresCreate.as_view(), name="vendedores_create"),
    path('vendedores_update/<int:pk>/', VendedoresUpdate.as_view(), name="vendedores_update"),
    path('vendedores_delete/<int:pk>/', VendedoresDelete.as_view(), name="vendedores_delete"),

#________________________Clientes
    path('Clientes/', ClientesList.as_view(), name="Clientes"),
    path('clientes_create/', ClientesCreate.as_view(), name="clientes_create"),
    path('clientes_update/<int:pk>/', ClientesUpdate.as_view(), name="clientes_update"),
    path('clientes_delete/<int:pk>/', ClientesDelete.as_view(), name="clientes_delete"),


#________________________Productos
    path('Productos/', ProductosList.as_view(), name="Productos"),
    path('productos_create/', ProductosCreate.as_view(), name="productos_create"),
    path('productos_update/<int:pk>/', ProductosUpdate.as_view(), name="productos_update"),
    path('productos_delete/<int:pk>/', ProductosDelete.as_view(), name="productos_delete"),
    path('buscar_productos/', buscarProductos, name="buscar_productos"),
    path('encontrar_productos/', encontrarProductos, name="encontrar_productos"),



#________________________Productos por mayor
    path('Productos_por_mayor/', ProductosPorMayorList.as_view(), name="Productos_por_mayor"),
    path('productos_por_mayor_create/', ProductosPorMayorCreate.as_view(), name="productos_por_mayor_create"),
    path('productos_por_mayor_update/<int:pk>/', ProductosPorMayorUpdate.as_view(), name="productos_por_mayor_update"),
    path('productos_por_mayor_delete/<int:pk>/', ProductosPorMayorDelete.as_view(), name="productos_por_mayor_delete"),

#________________________Login, logout, registro, editar perfil y agregar avatar
    path('login/',login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="Dietetica/logout.html") , name='logout'),
    path('registro/',register, name="registro"),
    path('editarPerfil/',EditProfile, name="editar_perfil"),
    path('<int:pk>/password/', CambiarClave.as_view() , name='cambiar_clave'),
    path('agregar_avatar/', agregarAvatar , name='agregar_avatar'),

#________________________Acerca de mi
    path('acerca_de_mi/', acerca_de_mi, name='acerca_de_mi'),
    ]
