# app_clientes/models.py

from django.db import models

# 1. MODELO ROL
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre_rol

# 2. MODELO CLIENTE (Completo con todos los atributos de tu tabla original)
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    
    # Clave foránea: Un Cliente tiene UN Rol (1:N)
    id_rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, verbose_name="Rol de Usuario")
    
    # 🟢 Atributos reincorporados
    nombre = models.CharField(max_length=100)
    ap_paterno = models.CharField(max_length=100)
    ap_materno = models.CharField(max_length=100, blank=True, null=True) # Puede ser opcional
    telefono = models.CharField(max_length=15, blank=True, null=True) # Puede ser opcional
    
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.ap_paterno} ({self.email})"
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

# NOTA: Direccion, Pedido, Producto y otros modelos fueron omitidos para este CRUD enfocado en Cliente.