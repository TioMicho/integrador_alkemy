from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'listado-productos.html', {'productos': productos})


def crear_producto(request):
    form = ProductoForm()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')

    return render(request, 'form-producto.html', {'form': form, 'submit': 'Crear producto'})


def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listado-proveedores.html', {'proveedores': proveedores})


def crear_proveedor(request):
    form = ProveedorForm()

    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores')

    return render(request, 'form-proveedor.html', {'form': form, 'submit': 'Crear proveedor'})


def home(request):
    return render(request, 'home.html')
