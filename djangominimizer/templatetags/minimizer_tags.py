import os
from django.template import Library
from djangominimizer.models import Minimizer
from djangominimizer import settings

register  = Library()


@register.inclusion_tag('minimizer/tags/javascripts.html', takes_context=True)
def minimizer_javascripts(context):
    arguments = {
        'STATIC_URL': context['STATIC_URL']
    }

    if not settings.MINIMIZER_DEBUG:
        try:
            minimizer = Minimizer.objects.latest()
            arguments.update({'scripts': []})

            for script in settings.SCRIPTS:
                script_min = ('-%s' % minimizer.script_name).join(
                    os.path.splitext(script))
                arguments.get('scripts').append(script_min)

                return arguments

        except Minimizer.DoesNotExist:
            pass

    arguments.update({'scripts': settings.SCRIPTS})

    return arguments
