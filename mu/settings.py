"""
Django settings for mu project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/

"""

import django_heroku
import os
import dj_database_url
#import dotenv
from pathlib import Path
import psycopg2.extensions

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#dotenv_file= os.path.join(BASE_DIR, '.env')

#if os.path.isfile(dotenv_file):
#    dotenv.load_dotenv(dotenv_file)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'f557wk)rd8_2i!yhgwmyu!ucu2k8=ce0!(df43233%+g_3((-)'
#xsSECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost','127.0.0.1','mu120tab.herokuapp.com/','77.53.56.197']

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'None' # Solved the problem with 'bool' lower() issue
CSRF_COOKIE_SECURE = True
#CSRF_COOKIE_DOMAIN = None   # In development
#CSRF_COOKIE_HTTPONLY = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mu',
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

ROOT_URLCONF = 'mu.urls'

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

WSGI_APPLICATION = 'mu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DATABASES = {}
#db_from_env = dj_database_url.config()
#DATABASES['default']=dj_database_url.config(conn_max_age=600)

# Use this in developement
# DATABASES = {  'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# In developpment using local postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8hmm8cfjp26t0',
        'USER': 'gxpkzvpjfrtomn',
        'PASSWORD': 'f49ce9403ec3d855ceccfd8384655d68f5e8e97e45a10625f9c36fc8c286893c',
        'HOST': 'ec2-54-247-71-245.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

WHITENOISE_USE_FINDERS = True

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



#STATICFILES_DIRS = [
#    os.path.join(os.path.dirname(BASE_DIR), "static", "static")
#]

# If images or other media
#MEDIA_URL = "/media/"
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


django_heroku.settings(locals())



