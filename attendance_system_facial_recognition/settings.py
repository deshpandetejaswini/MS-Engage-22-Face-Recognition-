"""
Django settings for attendance_system_facial_recognition project.
This file(settings.py file) contains all the configuration of  Django installation
 Django 2.2.2. is used
 
 
 
 Settings file is used to import values from other setting files,to allot the settings ,database settings, logging configuration,
 in dynamic way and it does not allow python syntax errors.


"""

import os


#BASE_DIR is a variable which is used so that there is portability in  this code and  it can work on different machines 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




# SECURITY WARNING: keep the secret key used in production secret!
# This value is the key to securing signed data
# to provide cryptographic signing
SECRET_KEY = '4!of@+5)(cu6!@c&21m644*%n5)h(9h6shzgg5ka%005e=04qu'

# SECURITY WARNING: don't run with debug turned on in production!
#debug=true is for debugging during development.
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# a list of Django apps within a project
INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'recognition.apps.RecognitionConfig',
     
    
    'crispy_forms' ,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#Middleware is like a middle ground between a request and response. It is like a window through which data passes
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'attendance_system_facial_recognition.urls'

#the templates folder is created and kept in the sample directory where manage.py lives. 

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

WSGI_APPLICATION = 'attendance_system_facial_recognition.wsgi.application'


# Database

#default database-sqlite3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# The list of validators that are used to check the strength of user’s passwords.

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
#allow web application for different app content languages

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# these files contains information which has to be displayed in  an app

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL='login'
LOGOUT_REDIRECT_URL = 'home'


LOGIN_REDIRECT_URL='dashboard'

