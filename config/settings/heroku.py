
import dj_database_url

from .base import *


DEBUG = True


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    *MIDDLEWARE
]


ALLOWED_HOSTS = [
    '.herokuapp.com'
]


DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
