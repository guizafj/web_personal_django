"""
Configuración principal de Django para el proyecto 'webpersonal'.

Este archivo contiene todas las configuraciones necesarias para el funcionamiento
del proyecto, incluyendo aplicaciones instaladas, middleware, bases de datos,
configuración de archivos estáticos y multimedia, internacionalización, y otros
ajustes relevantes.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.2/topics/settings/

Autor: Francisco J Diaz G
Fecha: 2025-04-25
"""

from pathlib import Path
import os

# Construye las rutas base del proyecto.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración rápida para desarrollo - no apta para producción.
# Verifica la documentación oficial para checklist de despliegue:
# https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# ¡IMPORTANTE! Mantén la clave secreta en secreto en producción.
SECRET_KEY = 'django-insecure-hxdb%*ww5a#ga)-@et834l1rk9zjzhmax=*)a0-5p9ve+_2cbt'

# ¡IMPORTANTE! No ejecutes con debug activado en producción.
DEBUG = True

# Lista de hosts permitidos para el despliegue.
ALLOWED_HOSTS = []

# Definición de aplicaciones instaladas en el proyecto.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Aplicación principal del proyecto.
    'portfolio.apps.PortfolioConfig',  # Configuración personalizada de la app 'portfolio'.
]

# Definición de middleware utilizado por el proyecto.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de las URLs principales del proyecto.
ROOT_URLCONF = 'webpersonal.urls'

# Configuración de plantillas (templates) para el proyecto.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Puedes agregar rutas personalizadas para tus plantillas aquí.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de la aplicación WSGI.
WSGI_APPLICATION = 'webpersonal.wsgi.application'

# Configuración de la base de datos.
# Por defecto, se utiliza SQLite3. Puedes cambiar la configuración para otros motores.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validadores de contraseñas para mejorar la seguridad.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de internacionalización.
LANGUAGE_CODE = 'es'  # Idioma por defecto: Español

TIME_ZONE = 'UTC'  # Zona horaria por defecto

USE_I18N = True  # Habilita la internacionalización

USE_TZ = True  # Habilita el uso de zonas horarias

# Configuración de archivos estáticos (CSS, JavaScript, Imágenes).
STATIC_URL = 'static/'

# Configuración de archivos multimedia (subidas de usuarios).
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Ruta donde se guardan los archivos multimedia

# Tipo de campo auto-incremental por defecto para modelos.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
