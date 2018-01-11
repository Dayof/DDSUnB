from .base import *

DEBUG = True
GOOGLE_ANALYTICS_TAG = 0

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddsunb',
        'USER':  get_env_variable('DATABASE_USER'),
        'PASSWORD':  get_env_variable('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
