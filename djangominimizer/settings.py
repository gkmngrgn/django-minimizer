import os
from django.conf import settings

MINIMIZER_DEBUG = getattr(settings, 'MINIMIZER_DEBUG', settings.DEBUG)
CLOSURE_PATH = getattr(settings, 'MINIMIZER_CLOSURE_PATH', '')
SCRIPTS = getattr(settings, 'MINIMIZER_SCRIPTS', [])
STYLES = getattr(settings, 'MINIMIZER_STYLES', [])
JQUERY_VERSION = getattr(settings, 'MINIMIZER_JQUERY_VERSION', '1.7')
DESCRIPTION = getattr(settings, 'MINIMIZER_DESCRIPTION', '')
AUTHOR = getattr(settings, 'MINIMIZER_AUTHOR', '')
GOOGLE_ANALYTICS_CODE = getattr(
    settings, 'MINIMIZER_GOOGLE_ANALYTICS_CODE', '')


# Tool settings
JS_PATH = os.path.join(settings.STATIC_ROOT, 'js')
TOOLS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tools'))
YUI_COMPRESSOR = 'yuicompressor-2.4.7.jar'
