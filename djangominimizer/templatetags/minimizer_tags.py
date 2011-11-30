import os
from django.template import Library
from djangominimizer import settings
from djangominimizer.models import Minimizer
from djangominimizer.utils import get_minimizer_list

register  = Library()


@register.inclusion_tag('minimizer/tags/styles.html', takes_context=True)
def minimizer_styles(context):
    arguments = {
        'STATIC_URL': context['STATIC_URL'],
        'styles': get_minimizer_list(settings.STYLES)
    }

    return arguments


@register.inclusion_tag('minimizer/tags/scripts.html', takes_context=True)
def minimizer_scripts(context):
    # FIXME: optimize it.
    scripts = []
    for script in get_minimizer_list(settings.SCRIPTS):
        is_coffee = os.path.splitext(script)[-1] == '.coffee'
        scripts.append([script, is_coffee])

    arguments = {
        'STATIC_URL': context['STATIC_URL'],
        'scripts': scripts
    }

    return arguments
