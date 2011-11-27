# -*- coding: utf-8 -*-
import os
import sys
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from settings_local import *

ROOT = os.path.abspath(os.path.dirname(__file__))
# it's required for including djangominimizer
sys.path.append(os.path.join(ROOT, '..'))

TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Gökmen Görgen', 'gokmen@alageek.com'),)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT, 'website.db')
    }
}
TIME_ZONE = 'Europe/Istanbul'
LANGUAGE_CODE = 'en'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (
    os.path.join(ROOT, 'static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder')
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader')
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware')
ROOT_URLCONF = 'urls'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd Party Applications
    'south',
    'djangominimizer',

    # Internal Application
    'base')
TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'djangominimizer.context_processors.minimizer_settings',
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Django Minimizer Settings
MINIMIZER_SCRIPTS = [
    'application.js'
]
MINIMIZER_STYLES = [
    'styles.css'
]
