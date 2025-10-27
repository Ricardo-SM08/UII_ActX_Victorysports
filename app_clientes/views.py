# app_clientes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Cliente, Rol
from .forms import ClienteForm

# CRUD - READ (Listar Clientes)
def index(request):
    """Muestra la lista de todos los clientes."""
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    # Asegúrate de haber resuelto el error TemplateDoesNotExist (Opción 1 o 2 del mensaje anterior)
    return render(request, 'app_clientes/index.html', context)

# CRUD - CREATE (Agregar Cliente)
def agregar(request):
    """Maneja el formulario para crear un nuevo cliente."""
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la lista después de guardar
            return redirect(reverse('index')) 
    else:
        # Petición GET: muestra el formulario vacío
        form = ClienteForm()
        
    context = {'form': form}
    return render(request, 'app_clientes/agregar.html', context)

# CRUD - UPDATE (Editar Cliente)
def editar(request, cliente_id):
    """Maneja el formulario para editar un cliente existente."""
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    
    if request.method == 'POST':
        # Instancia el formulario con los datos POST y la instancia del cliente
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            # Redirige a la lista después de actualizar
            return redirect(reverse('index'))
    else:
        # Petición GET: muestra el formulario precargado con los datos del cliente
        form = ClienteForm(instance=cliente)
        
    context = {'form': form, 'cliente_id': cliente_id}
    return render(request, 'app_clientes/editar.html', context)

# CRUD - DELETE (Eliminar Cliente)
def eliminar(request, cliente_id):
    """Ejecuta la acción de eliminar un cliente."""
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    
    if request.method == 'POST':
        cliente.delete()
    
    # Siempre redirige a la lista de clientes
    return redirect(reverse('index'))

# CRUD - READ (Función placeholder)
def ver_cliente(request, cliente_id):
    """Función placeholder para la URL de vista detallada (no renderiza, solo redirige)."""
    return redirect(reverse('index'))