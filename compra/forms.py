from django.forms import ModelForm
from .models import Producto, Proveedor


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'proveedor']


class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']
