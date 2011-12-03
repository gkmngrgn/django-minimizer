import time
from datetime import datetime
from django.core.cache import cache
from djangominimizer.settings import CACHE_TIMEOUT


class Cache:
    def __init__(self):
        self.prefix = 'djangominimizer'
        self.timestamp = self.__timestamp()

    def key(self, key):
        return 'djangominimizer.%s' % key

    def get_timestamp(self):
        return cache.get(self.key('timestamp'))

    def update_timestamp(self):
        return cache.set(self.key('timestamp'), self.timestamp,
                         timeout=CACHE_TIMEOUT)

    def __timestamp(self):
        now = datetime.now().timetuple()
        timestamp = int(time.mktime(now))

        return timestamp
