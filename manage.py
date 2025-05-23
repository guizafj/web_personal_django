#!/usr/bin/env python
"""
Utilidad de línea de comandos para tareas administrativas de Django.

Este archivo permite ejecutar tareas administrativas como iniciar el servidor de desarrollo,
aplicar migraciones, crear superusuarios, entre otras funciones propias del framework Django.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.2/ref/django-admin/

Autor: Francisco J Diaz G
Fecha: 2025-04-25
"""

import os
import sys


def main():
    """
    Ejecuta las tareas administrativas de Django.

    Establece la configuración por defecto del módulo de settings y ejecuta el
    comando recibido por línea de comandos.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webpersonal.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y disponible en tu variable "
            "de entorno PYTHONPATH? ¿Olvidaste activar un entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
