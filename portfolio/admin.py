"""
Módulo de configuración del panel de administración para la aplicación 'portfolio'.

Este módulo registra el modelo Project en el sitio de administración de Django,
permitiendo su gestión a través de la interfaz de administración. Además, define
una clase personalizada para mostrar ciertos campos como solo lectura.

Autor: Francisco J Diaz G
Fecha: 2025-04-25
"""

from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Project en el admin de Django.

    Atributos:
        readonly_fields (tuple): Campos que serán de solo lectura en el panel de administración.
    """
    readonly_fields = ('created', 'updated')  # Campos que solo se pueden leer en el admin

# Registra el modelo Project en el panel de administración con la configuración personalizada.
admin.site.register(Project, ProjectAdmin)

