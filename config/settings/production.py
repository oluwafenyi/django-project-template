
from .base import *


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE
]

# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# CORS_ORIGIN_ALLOW_ALL = False

# CORS_ALLOWED_ORIGINS = []

ALLOWED_HOSTS = [

]

DEBUG = False

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
    ),
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USERNAME"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
    }
}
