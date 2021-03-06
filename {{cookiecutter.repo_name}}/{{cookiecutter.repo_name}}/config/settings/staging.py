"""Development settings and globals."""

from __future__ import absolute_import

from .base import *

import os

########## DEBUG CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## DATABASE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_dev',
        'USER': 'django_dev',
        'PASSWORD': 'django_dev',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
########## END DATABASE CONFIGURATION


########## EMAIL CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## CACHE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHE_ENGINES = {
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'localhost:6379:0',
    },
    'dummy': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

CACHES = {
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'localhost:6379:0',
    }
}

CACHES['default'] = CACHE_ENGINES[os.getenv('CACHE', 'dummy')]

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
########## END CACHE CONFIGURATION d

########## LOGGING CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
LOGGERS = {
    # Log requests locally without [INFO] tag
    'werkzeug': {
        'handlers': ['default'],
        'level': 'DEBUG',
        'propagate': False,
    },
    # Log queue workers to console and file on development
    'rq.worker': {
        'handlers': ['default'],
        'level': 'DEBUG',
        'propagate': False,
    },
}

LOGGING['loggers'].update(LOGGERS)
########## END LOGGING CONFIGURATION


########## TOOLBAR CONFIGURATION
# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
########## END TOOLBAR CONFIGURATION


########## SSL SERVER CONFIGURATION
# https://github.com/teddziuba/django-sslserver#getting-started
INSTALLED_APPS += (
    'sslserver',
)
########## END SSL SERVER CONFIGURATION

try:
    from .local_settings import *
except:
    pass
