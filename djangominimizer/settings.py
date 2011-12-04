import os
from django.conf import settings

MINIMIZER_DEBUG = getattr(settings, 'MINIMIZER_DEBUG', settings.DEBUG)
COFFEE_SUPPORT = getattr(settings, 'MINIMIZER_COFFEE_SUPPORT', False)
CLOSURE_PATH = getattr(settings, 'MINIMIZER_CLOSURE_PATH', '')
SCRIPTS = getattr(settings, 'MINIMIZER_SCRIPTS', [])
STYLES = getattr(settings, 'MINIMIZER_STYLES', [])
JQUERY_VERSION = getattr(settings, 'MINIMIZER_JQUERY_VERSION', '1.7')
YUI_VERSION = getattr(settings, 'MINIMIZER_YUI_VERSION', '2.4.7')
DESCRIPTION = getattr(settings, 'MINIMIZER_DESCRIPTION', '')
AUTHOR = getattr(settings, 'MINIMIZER_AUTHOR', '')
GOOGLE_ANALYTICS_CODE = getattr(
    settings, 'MINIMIZER_GOOGLE_ANALYTICS_CODE', '')
CACHE_TIMEOUT = getattr(settings, 'MINIMIZER_CACHE_TIMEOUT', 1800)

# Tool settings
SCRIPTS_PATH = os.path.join(settings.STATIC_ROOT, 'scripts')
STYLES_PATH = os.path.join(settings.STATIC_ROOT, 'styles')
TOOLS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tools'))

COMMAND_YUI = os.path.join(TOOLS_PATH, 'yuicompressor-%s.jar' % YUI_VERSION)
COMMAND_COFFEE = os.path.join(
    TOOLS_PATH, 'node_modules', 'coffee-script', 'bin', 'coffee')
