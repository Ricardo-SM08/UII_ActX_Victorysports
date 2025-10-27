# app_clientes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # READ - Listado principal (Home)
    path('', views.index, name='index'), 
    
    # CREATE - Agregar Cliente
    path('agregar/', views.agregar, name='agregar'),
    
    # READ - Ver detalles (URL dinámica con PK)
    path('ver/<int:cliente_id>/', views.ver_cliente, name='ver_cliente'),
    
    # UPDATE - Editar Cliente (URL dinámica con PK)
    path('editar/<int:cliente_id>/', views.editar, name='editar'),
    
    # DELETE - Eliminar Cliente (URL dinámica con PK)
    path('eliminar/<int:cliente_id>/', views.eliminar, name='eliminar'),
]