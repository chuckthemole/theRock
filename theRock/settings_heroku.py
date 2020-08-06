import os
import dj_database_url
import django_heroku
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
#SECRET_KEY = '8ok#oll1qc4=2)hbr4afddmdp#z9ed274$_$pu_oe1x36!%lsi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["https://rocker-final-project.herokuapp.com/"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'rock.apps.rockConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'theRock.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'theRock.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# This setting allow us to use the Heroku DB locally
DATABASES = {
    'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES['default'] = dj_database_url.config()
DATABASES['default'] = dj_database_url.config(default='postgres://kbqvogagwdknwb:1a2bd480ba9997c8ee7982257e1aeb0dba9b33c2c93cc4736149dcb60743d710@ec2-52-207-93-32.compute-1.amazonaws.com:5432/de7sqp9uf3620a')
# The content of default= '  '   is  found in Heroku app URI, starts with postgres://...
# allow us to connect locally the DB is Heroku

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
# try runserver localy now
# python manage.py runserver


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
TATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'rock/static'),
)
django_heroku.settings(locals())
