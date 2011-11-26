from djangominimizer import settings
from djangominimizer.utils import get_script_path
from django.template import Library

register  = Library()


@register.inclusion_tag('minimizer/tags/javascripts.html', takes_context=True)
def minimizer_javascripts(context):
    arguments = {'STATIC_URL': context['STATIC_URL']}

    if settings.MINIMIZER_DEBUG:
        scripts = settings.SCRIPTS
    else:
        scripts = get_script_path()
        if not scripts:
            settings.MINIMIZER_DEBUG = True
            scripts = settings.SCRIPTS

    arguments.update({
        'DEBUG': settings.MINIMIZER_DEBUG,
        'scripts': scripts
    })

    return arguments
