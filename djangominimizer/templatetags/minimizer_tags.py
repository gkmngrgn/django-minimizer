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
    arguments = {
        'STATIC_URL': context['STATIC_URL'],
        'scripts': get_minimizer_list(settings.SCRIPTS)
    }

    return arguments
