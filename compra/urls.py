from django.urls import path
from compra import views


urlpatterns = [
    path('producto/listado', views.productos, name='productos'),
    path('producto/crear', views.crear_producto, name='crear-productos'),

    path('proveedor/listado', views.proveedores, name='proveedores'),
    path('proveedor/crear', views.crear_proveedor, name='crear-proveedores'),

    path('', views.home, name='home')
]
