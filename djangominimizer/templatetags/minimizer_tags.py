import os
from django.template import Library
from djangominimizer import settings
from djangominimizer.cache import Cache
from djangominimizer.utils import get_minimizer_list

register = Library()
cache = Cache()


@register.inclusion_tag('minimizer/tags/styles.html')
def minimizer_styles():
    timestamp = cache.get_timestamp()

    # FIXME: optimize it.
    styles = []
    for style in get_minimizer_list(settings.STYLES, timestamp, 'css'):
        is_less = os.path.splitext(style)[-1] == '.less'
        styles.append([style, is_less])

    arguments = {'styles': styles}

    return arguments


@register.inclusion_tag('minimizer/tags/scripts.html')
def minimizer_scripts():
    timestamp = cache.get_timestamp()

    # FIXME: optimize it.
    scripts = []
    for script in get_minimizer_list(settings.SCRIPTS, timestamp, 'js'):
        is_coffee = os.path.splitext(script)[-1] == '.coffee'
        scripts.append([script, is_coffee])

    arguments = {'scripts': scripts}

    return arguments
