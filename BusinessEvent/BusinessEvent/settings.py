"""
Django settings for BusinessEvent project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__)) + '/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oe+#yp3mb(v&&@v5$*4s!efeax2gu*6kx97^etyf@=#h7v-62#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'event/templates'),
)

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'event',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'BusinessEvent.urls'

WSGI_APPLICATION = 'BusinessEvent.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT + 'db/webapps.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = PROJECT_ROOT + 'media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# URL to use if the authentication system requires a user to log in.
LOGIN_URL = '/event'

# Default URL to redirect to after a user logs in.
LOGIN_REDIRECT_URL = '/event'

# Optional SMTP authentication information for EMAIL_HOST.
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'kuokuo001@gmail.com'
EMAIL_HOST_PASSWORD = '5675608Richardss'
EMAIL_USE_TLS = True
