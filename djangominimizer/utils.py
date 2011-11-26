import os
from django.conf import settings
from djangominimizer.models import Minimizer


def get_script_path():
    try:
        script_name = Minimizer.objects.latest().script_name
        js_path = os.path.join(settings.STATIC_ROOT, 'js', script_name)

        if not os.path.exists(js_path):
            return False

    except Minimizer.DoesNotExist:
        return False

    return script_name
