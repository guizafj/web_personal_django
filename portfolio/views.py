"""
Módulo de vistas para la aplicación 'portfolio'.

Este módulo define las vistas encargadas de gestionar las solicitudes HTTP
relacionadas con los proyectos del portafolio y de renderizar las respuestas
utilizando plantillas HTML.

Autor: Francisco J Diaz G
Fecha: 2025-04-25
"""

from django.shortcuts import render
from .models import Project

def portfolio(request):
    """
    Vista para mostrar la página del portafolio con todos los proyectos.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP.

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla 'portfolio/portfolio.html'
        y el listado de proyectos.
    """
    projects = Project.objects.all()  # Obtiene todos los proyectos de la base de datos
    return render(
        request,
        "portfolio/portfolio.html",
        {"projects": projects}  # Pasa los proyectos al contexto de la plantilla
    )