from .base import *

DEBUG = False
GOOGLE_ANALYTICS_TAG = 1

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddsunb',
        'USER': 'adm',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
