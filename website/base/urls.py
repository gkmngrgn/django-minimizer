from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from base.views import Index

urlpatterns = patterns(
    '',
    url(r'^$', view=Index.as_view(), name='index'))