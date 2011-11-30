REQUIREMENTS
============

- Java >= 1.4 (for YUI Compressor)
- Node >= 0.6.0 (for CoffeeSript compiler)
- Django >= 1.3.1
- South >= 0.7.3

INSTALLATION
============

- Add `djangominimizer` to INSTALLED_APPS.
- Add template context processor of djangominimizer:

::

    TEMPLATE_CONTEXT_PROCESSORS = (
        [...]
        'djangominimizer.context_processors.minimizer_settings'
    )

- If you are using CoffeeScript instead of Javascript, don't forget to add
this line to your `settings.py`:

::

    MINIMIZER_COFFEE_SUPPORT = True
