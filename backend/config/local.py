from .common import Common, BASE_DIR


class Local(Common):
    DEBUG = True
    ALLOWED_HOSTS = ["*"]

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ['django_nose']
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=backend'
    ]

    # EMAIL
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#email-host
    EMAIL_HOST = "localhost"
    # https://docs.djangoproject.com/en/dev/ref/settings/#email-port
    EMAIL_PORT = 1025
    # WhiteNoise
    # ------------------------------------------------------------------------------
    # http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
    INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405

    # Corsheaders
    CORS_ORIGIN_ALLOW_ALL = True

    # Your stuff...
    # ------------------------------------------------------------------------------

