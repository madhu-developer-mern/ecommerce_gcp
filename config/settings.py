"""
Django settings for SimpleShop backend.
"""
import os
from pathlib import Path
from datetime import timedelta

# Optional dotenv loading if .env file exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-simpleshop-dev-key-change-in-production-2026')

DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1', 'yes')

# Allowed Hosts configuration for local development and Cloud Run
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "ecommerce-gcp-733413941795.europe-west1.run.app",
]

# If an environment variable is set for ALLOWED_HOSTS, merge additional hosts
# while ensuring the required Cloud Run hostname and localhost are preserved
allowed_hosts_env = os.getenv("ALLOWED_HOSTS")
if allowed_hosts_env:
    for host in [h.strip() for h in allowed_hosts_env.split(",") if h.strip()]:
        if host not in ALLOWED_HOSTS:
            ALLOWED_HOSTS.append(host)

# CSRF Trusted Origins for Firebase Hosting and Cloud Run
CSRF_TRUSTED_ORIGINS = [
    "https://ecommerce-c34ed.web.app",
    "https://ecommerce-c34ed.firebaseapp.com",
    "https://ecommerce-gcp-733413941795.europe-west1.run.app",
]

# If an environment variable is set for CSRF_TRUSTED_ORIGINS, merge additional origins
csrf_trusted_env = os.getenv("CSRF_TRUSTED_ORIGINS")
if csrf_trusted_env:
    for origin in [o.strip() for o in csrf_trusted_env.split(",") if origin.strip()]:
        if origin not in CSRF_TRUSTED_ORIGINS:
            CSRF_TRUSTED_ORIGINS.append(origin)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',

    # Local apps
    'users.apps.UsersConfig',
    'products.apps.ProductsConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Top priority for CORS handling
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# Database: SQLite for local learning and simple stateless Cloud Run preparation
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Custom User Model
AUTH_USER_MODEL = 'users.User'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 6},
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

# SimpleJWT configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

# CORS Configuration for Firebase Hosting and Local Development
CORS_ALLOWED_ORIGINS = [
    "https://ecommerce-c34ed.web.app",
    "https://ecommerce-c34ed.firebaseapp.com",
    "http://localhost:5173",
]

# If an environment variable is set for CORS_ALLOWED_ORIGINS, merge additional origins
cors_env = os.getenv("CORS_ALLOWED_ORIGINS")
if cors_env:
    for origin in [o.strip() for o in cors_env.split(",") if o.strip()]:
        if origin not in CORS_ALLOWED_ORIGINS:
            CORS_ALLOWED_ORIGINS.append(origin)

CORS_ALLOW_CREDENTIALS = True
