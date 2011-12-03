import glob
import os
from django.core.cache import cache
from djangominimizer import settings
from djangominimizer.models import Minimizer


class Cache:
    def __init__(self):
        self.prefix = 'djangominimizer'

    def key(self, key):
        return 'djangominimizer.%s' % key

    def get_timestamp(self):
        timestamp = cache.get(self.key('timestamp'))
        if not timestamp:
            try:
                minimizer = Minimizer.objects.latest()
                timestamp = minimizer.timestamp

                # update timestamp information in cache.
                self.update_timestamp(minimizer.timestamp)
            except Minimizer.DoesNotExist:
                pass

        return timestamp

    def update_timestamp(self, timestamp):
        return cache.set(self.key('timestamp'), timestamp,
                         timeout=settings.CACHE_TIMEOUT)
