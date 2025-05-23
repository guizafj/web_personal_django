"""
Configuración de URLs para el proyecto 'webpersonal'.

Este archivo define las rutas principales del proyecto, asociando cada URL con
su vista correspondiente. También incluye la configuración para servir archivos
multimedia en modo desarrollo.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.2/topics/http/urls/

Autor: Francisco J Diaz G
Fecha: 2025-04-25
"""

from django.contrib import admin
from django.urls import path
from core import views as core_views
from django.conf import settings
from portfolio import views as portfolio_views

# Lista de patrones de URL del proyecto.
urlpatterns = [
    path('', core_views.home, name='home'),  # Página de inicio
    path('about-me/', core_views.about, name='about'),  # Página "Sobre mí"
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),  # Portafolio
    path('contact/', core_views.contact, name='contact'),  # Página de contacto
    path('admin/', admin.site.urls),  # Panel de administración de Django
]

# Configuración para servir archivos multimedia en modo desarrollo.
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)