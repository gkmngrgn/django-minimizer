from djangominimizer import settings


def minimizer_settings(request):
    """
    Adds minimizer_settings variables to the context.
    """
    context_data = {
        'MINIMIZER_JQUERY_VERSION': settings.JQUERY_VERSION,
        'MINIMIZER_DESCRIPTION': settings.DESCRIPTION,
        'MINIMIZER_AUTHOR': settings.AUTHOR
    }

    return context_data
