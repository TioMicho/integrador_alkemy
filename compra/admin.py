from django.contrib import admin
from .models import Proveedor, Producto


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dni')
    search_fields = ('nombre', 'apellido', 'dni')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'proveedor')
    search_fields = ('nombre', 'precio', 'proveedor')
