REQUIREMENTS
============

- Django >= 1.3.1
- South >= 0.7.3

INSTALLATION
============

- Add `djangominimizer` to INSTALLED_APPS.
- Add template context processor of djangominimizer:

    TEMPLATE_CONTEXT_PROCESSORS = (
        [...]
        'djangominimizer.context_processors.minimizer_settings'
    )
