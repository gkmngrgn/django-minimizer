Welcome to django-minimizer's documentation!
============================================
Django Minimizer compresses static files and provides html5 layout that is ready for extending to your project templates. It uses YUI compressor for compressing static files, and it has included Javascript files like modernizr, jquery, etc. Base template created with html5boilerplate.

This application also supports CoffeScript and LessCSS optionally. If you prefer to use CoffeeScript or LessCSS, you'll need to Node for compiling static files to .js or .css.

Requirements
------------
Django Minimizer has no dependency other than Django, but it needs to a cache_backend for getting compressed file timestamp information. If you prefer memcached, install `python-memcached` package.

::

    pip install -r requirements.txt

Other dependencies:

- Java >= 1.4 (for YUI Compressor)
- Node >= 0.6.0 (for CoffeeSript compiler)

Installation
------------
- Add `djangominimizer` to INSTALLED_APPS.
- Add required template context processors for djangominimizer:

::

    TEMPLATE_CONTEXT_PROCESSORS = (
        [...]
        'django.core.context_processors.request',
        'djangominimizer.context_processors.minimizer_settings'
    )

- Then, you should configure your cache_backend. For example:

::

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': [
                '127.0.0.1:11211'
            ]
        }
    }

- If you are using CoffeeScript instead of Javascript, don't forget to add
  this line to your `settings.py`:

::

    MINIMIZER_COFFEE_SUPPORT = True

Contents
--------

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
