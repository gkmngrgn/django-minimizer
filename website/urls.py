from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import include
from django.conf.urls.defaults import url

urlpatterns = patterns(
    '',
    url(r'^', include('base.urls')))
