from djangominimizer import settings


def minimizer_settings(request):
    """
    Adds minimizer_settings variables to the context.
    """
    context_data = {
        'MINIMIZER_COFFEE_SUPPORT': settings.COFFEE_SUPPORT,
        'MINIMIZER_DEBUG': settings.MINIMIZER_DEBUG,
        'MINIMIZER_JQUERY_VERSION': settings.JQUERY_VERSION,
        'MINIMIZER_DESCRIPTION': settings.DESCRIPTION,
        'MINIMIZER_AUTHOR': settings.AUTHOR,
        'MINIMIZER_GOOGLE_ANALYTICS_CODE': settings.GOOGLE_ANALYTICS_CODE
    }

    return context_data
