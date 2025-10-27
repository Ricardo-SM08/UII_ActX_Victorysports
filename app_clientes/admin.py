# app_clientes/admin.py

from django.contrib import admin
from .models import Rol, Cliente

admin.site.register(Rol)
admin.site.register(Cliente)