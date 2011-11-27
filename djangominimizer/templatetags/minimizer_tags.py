import os
from django.template import Library
from djangominimizer import settings
from djangominimizer.models import Minimizer
from djangominimizer.utils import get_minimizer_list

register  = Library()


@register.inclusion_tag('minimizer/tags/javascripts.html', takes_context=True)
def minimizer_javascripts(context):
    arguments = {
        'STATIC_URL': context['STATIC_URL']
        'scripts': get_minimizer_list(settings.SCRIPTS)
    }

    return arguments
