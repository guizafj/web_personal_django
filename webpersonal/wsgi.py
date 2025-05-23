"""
Configuración WSGI para el proyecto 'webpersonal'.

Este archivo expone la variable 'application' a nivel de módulo, que representa
la interfaz WSGI (Web Server Gateway Interface) utilizada para desplegar el
proyecto Django en servidores compatibles con WSGI.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/

Autor: Francisco J Diaz G
Fecha: 2025-04-25
"""

import os

from django.core.wsgi import get_wsgi_application

# Establece la configuración por defecto del módulo de settings de Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webpersonal.settings')

# Obtiene la aplicación WSGI que será utilizada por el servidor.
application = get_wsgi_application()
