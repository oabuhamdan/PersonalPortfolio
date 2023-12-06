from .base import *

DEBUG = False

INSTALLED_APPS += [
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
domain_name = os.environ.get("DOMAIN_NAME")
CSRF_TRUSTED_ORIGINS = ['https://localhost', 'https://*.127.0.0.1', f"https://{domain_name}",
                        f"https://*.{domain_name}"]
ALLOWED_HOSTS = ['localhost', '127.0.0.1', f".{domain_name}"]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.environ.get("LOGGING_PATH", os.path.join(BASE_DIR, "django.logs")),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
if os.environ.get("USE_SQL_LITE_IN_PRODUCTION", False) == "True":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.environ.get("SQL_LITE_PATH", os.path.join(BASE_DIR, "db.sqlite3")),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
            "NAME": os.environ.get("SQL_DATABASE", "database"),
            "USER": os.environ.get("SQL_USER", "user"),
            "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
            "HOST": os.environ.get("SQL_HOST", "localhost"),
            "PORT": os.environ.get("SQL_PORT", "5432"),
            "CONN_MAX_AGE": 60,
        }
    }

MEDIA_ROOT = os.environ.get("MEDIA_PATH", os.path.join(BASE_DIR, "media/"))
MEDIA_URL = os.environ.get("MEDIA_PATH", os.path.join(BASE_DIR, "media/"))
