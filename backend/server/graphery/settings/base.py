"""
Django settings for graphery project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILE_STORE_ROOT = Path('/var/www/')

AUTH_USER_MODEL = 'backend.User'

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sitemaps',
]

THIRD_PARTY_APPS = [
    'graphene_django',
    'django_filters',
    'corsheaders',
    'channels',
]

MY_APPS = [
    'backend.apps.BackendConfig',
]

# Application definition
INSTALLED_APPS = BASE_APPS + THIRD_PARTY_APPS + MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # TODO add gzip middleware? or use nginx gzip?
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'graphery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'graphery.wsgi.application'
ASGI_APPLICATION = 'graphery.routing.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

CSRF_COOKIE_SAMESITE = 'strict'

# GraphQL settings
GRAPHENE = {
    'SCHEMA': 'graphery.schema.schema',
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'

STATIC_FOLDER_NAME = 'graphery_static'

# To be changed
STATIC_ROOT = str(FILE_STORE_ROOT / STATIC_FOLDER_NAME)

# CORS_ORIGIN_WHITELIST = ['http://localhost:8080']

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
]

CORS_ALLOW_CREDENTIALS = True

UPLOAD_STATICS_ENTRY = 'upload'

UPLOAD_FOLDER_NAME = 'graphery_upload'

MEDIA_ROOT = str(FILE_STORE_ROOT / UPLOAD_FOLDER_NAME)

INVITATION_CODE_FOLDER = str(FILE_STORE_ROOT)

DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}
