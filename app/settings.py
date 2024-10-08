from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p(i!c^m%8+&yb)rtn8rdrv1rcaed-hw5e-+580x!r6imky62sl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rolepermissions',
    'users',
    'payments',
    
    # 'django_q'
]

# configuração para sobrescrevendo o metodo AbstractUser para criar o cpf
AUTH_USER_MODEL = 'users.User'

# Permissoes para usuarios
ROLEPERMISSIONS_MODULE = 'app.roles'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# MOCKYS para testes de autorizaçoes de serviço 
# AUTHORIZE_TRANSFER_ENDPOINT = "https://run.mocky.io/v3/3465d2ee-429a-471b-8495-062a8f28b728"  #error
AUTHORIZE_TRANSFER_ENDPOINT = "https://run.mocky.io/v3/d566d18d-4168-4c76-86a4-a83ab4d7b077" #success


# Mocky service authorized
"https://run.mocky.io/v3/d566d18d-4168-4c76-86a4-a83ab4d7b077"

# Mocky service unauthorized
"https://run.mocky.io/v3/3465d2ee-429a-471b-8495-062a8f28b728"

# URL para criar seu Mocky
"https://designer.mocky.io/design"


# OBS: o orm era necessario usar um banco em memoria como o Redis
# CLUSTER PARA ENVIO DE NOTIFICAÇÂO com => django-q
# Q_CLUSTER = {
#     'name': 'DjangoQ',
#     'workers': 4,
#     'timeout': 30,
#     'retry': 300,
#     'orm': 'default'
# }

from huey import SqliteHuey

HUEY = SqliteHuey(filename='huey.db')  # Especificando o arquivo SQLite para o Huey
