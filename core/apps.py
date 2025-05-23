"""
Módulo de configuración de la aplicación 'core'.

Este módulo define la configuración principal de la aplicación 'core' para el
proyecto Django. Permite personalizar ciertos aspectos del comportamiento de la
aplicación, como el nombre y el tipo de campo auto-incremental por defecto.

Autor: Francisco J Diaz G
Fecha: 2025-04-25
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Configuración de la aplicación 'core'.

    Atributos:
        default_auto_field (str): Especifica el tipo de campo auto-incremental
            por defecto para los modelos de la aplicación.
        name (str): Nombre de la aplicación, utilizado por Django para
            identificarla internamente.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
