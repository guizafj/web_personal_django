"""
Módulo de vistas para la aplicación 'core'.

Este módulo define las vistas principales de la aplicación 'core', encargadas de
gestionar las solicitudes HTTP y devolver las respuestas adecuadas utilizando
plantillas HTML. Cada vista corresponde a una sección de la web personal.

Autor: Francisco J Diaz G
Fecha: 2025-04-25
"""

from django.shortcuts import render, HttpResponse

# Variable con el menú de navegación en HTML (no utilizada actualmente).
html_base = """<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/about-me/">Sobre mi</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>"""


def home(request):
    """
    Vista para la página de inicio.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP.

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla 'core/home.html'.
    """
    return render(request, "core/home.html")


def about(request):
    """
    Vista para la página 'Sobre mí'.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP.

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla 'core/about-me.html'.
    """
    return render(request, "core/about-me.html")


def contact(request):
    """
    Vista para la página de contacto.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP.

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla 'core/contact.html'.
    """
    return render(request, "core/contact.html")