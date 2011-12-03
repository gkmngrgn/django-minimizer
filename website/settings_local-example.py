DEBUG = False
STATIC_ROOT = ''
SECRET_KEY = 't_blv5+g%9x58alu4rv49zi$rpl4njpjp2g_s&8(2qwd%t2en_'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '127.0.0.1:11211'
        ]
    }
}
