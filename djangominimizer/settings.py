from django.conf import settings

MINIMIZER_DEBUG = getattr(settings, 'MINIMIZER_DEBUG', settings.DEBUG)
SCRIPTS = getattr(settings, 'MINIMIZER_SCRIPTS', [])
JQUERY_VERSION = getattr(settings, 'MINIMIZER_JQUERY_VERSION', '1.7')
DESCRIPTION = getattr(settings, 'MINIMIZER_DESCRIPTION', '')
AUTHOR = getattr(settings, 'MINIMIZER_AUTHOR', '')
GOOGLE_ANALYTICS_CODE = getattr(
    settings, 'MINIMIZER_GOOGLE_ANALYTICS_CODE', '')
