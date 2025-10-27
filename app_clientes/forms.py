# app_clientes/forms.py

from django import forms
from .models import Cliente, Rol

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # Excluimos la PK y la fecha_registro (se llenan automáticamente)
        exclude = ('id_cliente', 'fecha_registro',)
        
        # 🟢 Uso de Widgets para aplicar estilos de Bootstrap 5
        widgets = {
            'id_rol': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ap_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'ap_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'id_rol': 'Rol de Usuario',
            'nombre': 'Nombre',
            'ap_paterno': 'Apellido Paterno',
            'ap_materno': 'Apellido Materno',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'password': 'Contraseña',
        }