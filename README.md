# Web Personal - Proyecto Django

Este proyecto es una aplicación web personal desarrollada con el framework Django. Incluye funcionalidades como un portafolio de proyectos, una página de contacto, y una sección "Sobre mí". Está diseñado para ser fácilmente extensible y personalizable.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Características

- **Página de inicio**: Información general sobre el sitio.
- **Sección "Sobre mí"**: Información personal.
- **Portafolio**: Listado de proyectos con título, descripción, imagen y enlace.
- **Página de contacto**: Formulario para que los usuarios puedan contactarte.
- **Panel de administración**: Gestión de proyectos y contenido dinámico.

---

## Requisitos

- Python 3.10 o superior
- Django 4.2.5
- Dependencias adicionales (ver `requirements.txt`):
  - `django-crispy-forms`
  - `Pillow`
  - `requests`

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/webpersonal.git
   cd webpersonal
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```

5. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

6. Accede al sitio en tu navegador en `http://127.0.0.1:8000`.

---

## Estructura del Proyecto

```plaintext
webpersonal/
├── core/                  # Aplicación principal
│   ├── admin.py           # Configuración del panel de administración
│   ├── apps.py            # Configuración de la aplicación
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas de la aplicación
│   ├── templates/         # Plantillas HTML
│   └── tests.py           # Pruebas unitarias
├── portfolio/             # Aplicación para el portafolio
│   ├── admin.py           # Configuración del panel de administración
│   ├── apps.py            # Configuración de la aplicación
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas de la aplicación
│   ├── templates/         # Plantillas HTML
│   └── tests.py           # Pruebas unitarias
├── webpersonal/           # Configuración del proyecto
│   ├── settings.py        # Configuración global del proyecto
│   ├── urls.py            # Configuración de rutas
│   ├── wsgi.py            # Configuración WSGI
│   └── asgi.py            # Configuración ASGI
├── manage.py              # Utilidad de línea de comandos de Django
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación del proyecto
```

---

## Uso

### Panel de Administración
1. Crea un superusuario para acceder al panel de administración:
   ```bash
   python manage.py createsuperuser
   ```
2. Accede al panel en `http://127.0.0.1:8000/admin`.

### Gestión de Proyectos
- Desde el panel de administración, puedes agregar, editar o eliminar proyectos que se mostrarán en la sección de portafolio.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz un commit (`git commit -m "Agrega nueva funcionalidad"`).
4. Envía tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request en este repositorio.

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](https://opensource.org/licenses/MIT). Puedes usarlo, modificarlo y distribuirlo libremente, siempre y cuando incluyas la licencia original.

---

## Autor

Desarrollado por **[F Javier]**. Si tienes preguntas o sugerencias, no dudes en contactarme.