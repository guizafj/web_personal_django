"""
Módulo de configuración de la aplicación 'portfolio'.

Este módulo define la configuración principal de la aplicación 'portfolio' para el
proyecto Django. Permite personalizar ciertos aspectos del comportamiento de la
aplicación, como el nombre, el nombre visible en el admin y el tipo de campo
auto-incremental por defecto.

Autor: Francisco J Diaz G
Fecha: 2025-04-25
"""

from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    """
    Configuración de la aplicación 'portfolio'.

    Atributos:
        default_auto_field (str): Especifica el tipo de campo auto-incremental
            por defecto para los modelos de la aplicación.
        name (str): Nombre interno de la aplicación, utilizado por Django.
        verbose_name (str): Nombre legible que se mostrará en el panel de administración.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name = 'Portafolio'  # Nombre que se mostrará en el admin
