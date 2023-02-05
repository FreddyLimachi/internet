

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.setdefault('SECRET_KEY', 'django-insecure-5d)ghzl(=i*q+pfd7wq&-=0_=4v!@f_2@y@2-d5+ao8-kh4baa'),
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.setdefault('DEBUG', 'True')

ALLOWED_HOSTS = ['internet-papuchin.up.railway.app', 'https://web-production-cd40.up.railway.app',]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'simple_history',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'internet.urls'

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

WSGI_APPLICATION = 'internet.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.setdefault('DB_NAME', 'internet'),
        'USER': os.environ.setdefault('DB_USER', 'postgres'),
        'PASSWORD': os.environ.setdefault('DB_PASSWORD', 'password'),
        'HOST': os.environ.setdefault('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.setdefault('DB_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CSRF_TRUSTED_ORIGINS = [
    'https://web-production-cd40.up.railway.app',
    'https://internet-papuchin.up.railway.app'
    ]

JAZZMIN_UI_TWEAKS = {
    "theme": "pulse",
}

JAZZMIN_SETTINGS = {
    "site_title": "Internet Papuchin",
    "site_header": "Internet Papuchin",
    "site_brand": "Internet Papuchin",

    #"site_logo": 'logos/logo.png',

    "welcome_sign": "Bienvenido al panel de administrador",
    "copyright": "Internet Papuchin",    
    "site_logo_classes": "AAS",
    "user_avatar": None,
    #"login_logo": 'logos/logo.png',


    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://www.google.com", "new_window": True},
        {"model": "auth.user"}
    ],

    "navigation_expanded": True,
}

ICON_EDIT_URL = 'https://cdn.discordapp.com/attachments/913266032301461534/1058395464690585701/category-search-3829.png'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = 'static/'
STATICFILES_DIRS = (BASE_DIR, 'static')
