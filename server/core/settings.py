"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import sys
from dotenv import load_dotenv
from datetime import  datetime, timedelta

import cloudinary
import cloudinary.uploader
import cloudinary.api


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Determine whether the environment is set to development or production
ENVIRONMENT = os.getenv("PY_ENV", "development")


# Load environment-specific .env file
if ENVIRONMENT == "test":
    dotenv_path = os.path.join(BASE_DIR, '.env.test')
elif ENVIRONMENT == "development":
    dotenv_path = os.path.join(BASE_DIR, '.env.development')
else:
    dotenv_path = os.path.join(BASE_DIR, '.env')

load_dotenv(dotenv_path)

cloudinary.config(
  cloud_name = os.environ["CLOUDINARY_CLOUD_NAME"],
  api_key = os.environ["CLOUDINARY_API_KEY"],
  api_secret = os.environ["CLOUDINARY_API_SECRET"],
  secure = True
)




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ["PY_ENV"] == "development" else False

host_list = [os.getenv("FRONTEND_URL"), 'localhost', '127.0.0.1']
if ENVIRONMENT == "test":
    host_list.append("testserver")

ALLOWED_HOSTS = host_list


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #External
    'graphene_django',
    'corsheaders',

    # Internal
    'account',
    'blog',
    'forum',
    'career',
    'service',
    'course'
]

# GraphQL Schema Path
GRAPHENE = {
    "SCHEMA": "core.schema.schema",
    "MIDDLEWARE": [],
}

JWT_EXPIRATION_DELTA = timedelta(days=1)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",

]

JWT_ACCESS_TOKEN_EXPIRATION_DELTA = timedelta(minutes=15)
JWT_REFRESH_TOKEN_EXPIRATION_DELTA = timedelta(days=1)

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'account', 'templates')],
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

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    os.environ["FRONTEND_URL"]
]

AUTH_USER_MODEL = 'account.User'

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases




# Define the database settings for development and production
if ENVIRONMENT == "development":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif ENVIRONMENT == "test":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'dbtest.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ["POSTGRES_ENGINE"],
            'NAME':  os.environ["SUPABASE_DB"],
            'USER': os.environ["SUPABASE_DB_USER"],
            'PASSWORD': os.environ["SUPABASE_DB_PASSWORD"],
            'HOST': os.environ["SUPABASE_DB_HOST"],
            'PORT': os.environ["SUPABASE_DB_PORT"],
        }
    }


if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'test_db.sqlite3',
        }
    }

# Use the SMTP backend for sending emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Gmail SMTP settings
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = 587  # Use TLS (587) or SSL (465)
EMAIL_USE_TLS = True if os.getenv("EMAIL_USE_TLS") == "True" else False
EMAIL_USE_SSL = True if not DEBUG else False
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# Default "from" address for outgoing emails
SERVER_EMAIL = os.getenv("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER")


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
