# -*- coding: utf-8 -*-
SECRET_KEY = "<key/should be inserted automatically>"
SERVICE_URL = "https://seafile.mydomain.com"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub_db',
        'USER': 'seafile',
        'PASSWORD': '<should be inserted automatically>',
        'HOST': 'seafile-mariadb',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'memcached:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
COMPRESS_CACHE_BACKEND = 'locmem'

TIME_ZONE = 'Europe/Berlin'
CSRF_TRUSTED_ORIGINS = ["https://seafile.mydomain.com"]
FILE_SERVER_ROOT = 'https://seafile.mydomain.com/seafhttp'
# DEBUG=True
ALLOWED_HOSTS = ['127.0.0.1','.mydomain.com']