# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

VERSION = '0.1'
DESCRIPTION = """\
Django application for minimizing static files and using simple html5 template
 with jQuery and modernizr."""

setup(
    name='django-minimizer',
    version=VERSION,
    description=DESCRIPTION,
    url='http://django-minimizer.alageek.com',
    author='Gökmen Görgen',
    author_email='gokmen@alageek.com',
    packages=find_packages(exclude=('website', 'website.*')),
    include_package_data=True,
    license='GPLv3',
    keywords='django application html5 yui compressor jquery modernizr',
    install_requires=[
        'Django>=1.3',
    ]
)
