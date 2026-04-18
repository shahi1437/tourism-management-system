from pathlib import Path

# =====================
# BASE CONFIG
# =====================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-change-this-key'

DEBUG = True

ALLOWED_HOSTS = []


# =====================
# APPLICATIONS
# =====================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your app
    'core',
]


# =====================
# MIDDLEWARE
# =====================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =====================
# URLS
# =====================
ROOT_URLCONF = 'tourism.urls'


# =====================
# TEMPLATES
# =====================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =====================
# WSGI
# =====================
WSGI_APPLICATION = 'tourism.wsgi.application'


# =====================
# DATABASE
# =====================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =====================
# PASSWORD VALIDATION
# (optional - keeps simple login like you want)
# =====================
AUTH_PASSWORD_VALIDATORS = []


# =====================
# LANGUAGE / TIME
# =====================
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True
USE_TZ = True


# =====================
# STATIC FILES
# =====================
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']


# =====================
# MEDIA FILES (images)
# =====================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =====================
# DEFAULT AUTO FIELD
# =====================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =====================
# AUTH SETTINGS (IMPORTANT)
# =====================
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'