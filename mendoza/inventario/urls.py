from django.contrib import admin
from django.urls import path
from . import views
from .views import grupolistar, grupoguardar, grupomodificar
from .views import clientelistar, clienteguardar, clientemodificar, proveedorlistar, proveedorguardar, proveedormodificar, productoguardar, productomodificar
urlpatterns = [
    path('grupolistar', grupolistar.as_view() , name='grupolistar'),
    path('grupoguardar', grupoguardar.as_view() , name='grupoguardar'),
    path('holapdf', views.hello_pdf, name='holapdf'),
    path('grupospdf', views.grupos_print, name='grupospdf'),
    path('grupoindividual/<int:pk>', views.grupos_print, name='grupoindividual'),
    path('grupomodificar/<int:pk>',views.grupomodificar.as_view() ,name='grupomodificar'),
####################CLIENTES################################
    path('clientelistar', clientelistar.as_view(), name='clientelistar'),
    path('clienteguardar', clienteguardar.as_view(), name='clienteguardar'),
    path('clientemodificar/<int:pk>', clientemodificar.as_view(), name='clientemodificar'),
    path('clientespdf', views.cliente_print, name='clientespdf'),
    path('clienteindividual/<int:pk>', views.cliente_print, name='clienteindividual'),
#######################proveedor#############################
    path('proveedorlistar', proveedorlistar.as_view(), name='proveedorlistar'),
    path('proveedorguardar', proveedorguardar.as_view(), name='proveedorguardar'),
    path('proveedormodificar/<int:pk>', proveedormodificar.as_view(), name='proveedormodificar'),
    path('proveedorpdf', views.proveedor_print, name='proveedorpdf'),
    path('proveedorindividual/<int:pk>', views.proveedor_print, name='proveedorindividual'),
#############################Producto########################
    path('productolistar',views.productolistar.as_view(), name='productolistar'),
    path('productoguardar',views.productoguardar.as_view(), name='productoguardar'),
    path('productomodificar/<int:pk>',views.productomodificar.as_view(), name='productomodificar'),
    path('productopdf',views.producto_print, name='productopdf'),
    path('productoindividual/<int:pk>', views.producto_print, name='productoindividual'),
]