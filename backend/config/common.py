from pathlib import Path

import dj_database_url
import environ
from configurations import Configuration

ROOT_DIR = Path(__file__).parents[2]
BASE_DIR = Path(__file__).parents[1]


def read_env():
    env = environ.Env()
    if env.bool("DJANGO_READ_DOT_ENV_FILE", default=False):
        # OS environment variables take precedence over variables from .secrets
        env.read_env(str(ROOT_DIR / ".env"))
    return env


class Common(Configuration):
    Env = read_env()

    DJANGO_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]

    THIRD_PARTY_APPS = [
        "rest_framework",
        "rest_framework.authtoken",
        "corsheaders",
        "django_filters",
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "dj_rest_auth",
        "dj_rest_auth.registration",
        "django_extensions",
    ]

    LOCAL_APPS = ["backend.users", "chat.apps.ChatConfig"]

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        "django.middleware.security.SecurityMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    )

    SITE_ID = 1

    ROOT_URLCONF = "backend.urls"
    SECRET_KEY = Env(
        "DJANGO_SECRET_KEY",
        default="kwkgSeC6K+npf6paVstmYyVY5JrH6SO2RzMN2xHFzkkLlSpbZ/m/zmj6Ig==",
    )
    WSGI_APPLICATION = "backend.wsgi.application"

    # Email
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

    ADMINS = (("Tobi DEGNON", "contact@djchat.com"),)

    # Postgres
    DATABASES = {
        "default": dj_database_url.config(
            default="postgres:///djchat",
            conn_max_age=Env.int("POSTGRES_CONN_MAX_AGE", 600),
        )
    }
    DATABASES["default"]["ATOMIC_REQUESTS"] = True

    # General
    APPEND_SLASH = False
    TIME_ZONE = "Africa/Porto-Novo"
    LANGUAGE_CODE = "en-us"
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = "/"

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = str(ROOT_DIR / "static")
    STATICFILES_DIRS = []
    STATIC_URL = "/static/"
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )

    # Media files
    MEDIA_ROOT = str(ROOT_DIR / "media")
    MEDIA_URL = "/media/"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": STATICFILES_DIRS,
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = Env.bool("DJANGO_DEBUG", default=False)

    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
    ]

    # Logging
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "django.server": {
                "()": "django.utils.log.ServerFormatter",
                "format": "[%(server_time)s] %(message)s",
            },
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
            },
            "simple": {"format": "%(levelname)s %(message)s"},
        },
        "filters": {
            "require_debug_true": {"()": "django.utils.log.RequireDebugTrue", },
        },
        "handlers": {
            "django.server": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "django.server",
            },
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "simple",
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
            },
        },
        "loggers": {
            "django": {"handlers": ["console"], "propagate": True, },
            "django.server": {
                "handlers": ["django.server"],
                "level": "INFO",
                "propagate": False,
            },
            "django.request": {
                "handlers": ["mail_admins", "console"],
                "level": "ERROR",
                "propagate": False,
            },
            "django.db.backends": {"handlers": ["console"], "level": "INFO"},
        },
    }

    # Custom user app
    AUTH_USER_MODEL = "users.User"

    # Django Rest Framework
    REST_FRAMEWORK = {
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": Env.int("DJANGO_PAGINATION_LIMIT", 10),
        "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
        "DEFAULT_RENDERER_CLASSES": (
            "rest_framework.renderers.JSONRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
        ),
        "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated", ],
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
        ),
    }

    # Rest auth
    # ------------------------------------------------------------------------------
    ACCOUNT_EMAIL_VERIFICATION = "none"
