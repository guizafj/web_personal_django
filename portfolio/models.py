"""
Módulo de modelos para la aplicación 'portfolio'.

Este módulo define el modelo Project, que representa los proyectos del portafolio
personal. Cada instancia de Project corresponde a un proyecto con título,
descripción, imagen, enlace y fechas de creación y modificación.

Autor: Francisco J Diaz G
Fecha: 2025-04-25
"""

from django.db import models

class Project(models.Model):
    """
    Modelo que representa un proyecto del portafolio.

    Campos:
        title (CharField): Título del proyecto.
        description (TextField): Descripción detallada del proyecto.
        image (ImageField): Imagen asociada al proyecto, almacenada en la carpeta 'projects'.
        link (URLField): Enlace externo relacionado con el proyecto (opcional).
        created (DateTimeField): Fecha y hora de creación del proyecto (asignada automáticamente).
        updated (DateTimeField): Fecha y hora de la última modificación (asignada automáticamente).
    """

    title = models.CharField(
        max_length=200,
        verbose_name='Título'
    )
    description = models.TextField(
        verbose_name='Descripción'
    )
    image = models.ImageField(
        verbose_name='Imagen',
        upload_to='projects'  # Carpeta donde se guardarán las imágenes
    )
    link = models.URLField(
        verbose_name='URL',
        null=True,
        blank=True  # Campo opcional
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de modificación'
    )

    class Meta:
        """
        Metadatos del modelo Project.

        verbose_name: Nombre singular para el modelo en el admin.
        verbose_name_plural: Nombre plural para el modelo en el admin.
        ordering: Orden por defecto de los registros (más recientes primero).
        """
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']

    def __str__(self):
        """
        Representación en cadena del objeto Project.

        Returns:
            str: Título del proyecto.
        """
        return self.title

