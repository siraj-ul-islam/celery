"""
Django settings for proj project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4k5(a-z0fcnfdxczbokyp)r7&usp1sv&#=i=no4a9j36r&27f_'

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
'django_celery_beat',
    'app1',
    'app2',
    'app3',
    'django_celery_results'

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

ROOT_URLCONF = 'proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/home/aitomation/Documents/django/celery/templates'],
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

WSGI_APPLICATION = 'proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# CELERY_ALWAYS_EAGER = True
# gmail_send/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sirajkhanmardan123@gmail.com'
EMAIL_HOST_PASSWORD = 'zhddpjtiesprccsa'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'sirajkhanmardan123@gmail.com'


# CELERY_BEAT_SCHEDULE = {
# # "scheduled_task": {
# #         "task": "app2.tasks.send_review_email_task",
# #         "schedule": 10.0,
# #         "args": ("siraj", "sirajkhanmardan123@gmail.com","Good"),
# #     },
#     "scheduled_task": {
#         "task": "add_2_number_task",
#         "schedule": 5.0,
#         "args": (10, 10),
#     },
#     # "database": {
#     #     "task": "app3.tasks.bkup",
#     #     "schedule": 5.0,
#     # },
# }
CELERY_RESULT_BACKEND = 'django-db'
""" crontab() Execute every minute.
crontab(minute=0, hour=0) Execute daily at midnight.
crontab(minute=0, hour='*/3') Execute every three hours: midnight, 3am, 6am, 9am, noon, 3pm, 6pm, 9pm.
crontab(minute=0, hour='0,3,6,9,12,15,18,21') Same as previous.
crontab(minute='*/15') Execute every 15 minutes.
crontab(day_of_week='sunday') Execute every minute (!) at Sundays.
crontab(minute='*', hour='*', day_of_week='sun') Same as previous.
crontab(minute='*/10', hour='3,17,22', day_of_week='thu,fri') Execute every ten minutes, but only between 3-4 am, 5-6 pm, and 10-11 pm on Thursdays or Fridays.
crontab(minute=0, hour='*/2,*/3') Execute every even hour, and every hour divisible by three. This means: at every hour except: 1am, 5am, 7am, 11am, 1pm, 5pm, 7pm, 11pm
crontab(minute=0, hour='*/5') Execute hour divisible by 5. This means that it is triggered at 3pm, not 5pm (since 3pm equals the 24-hour clock value of “15”, which is divisible by 5).
crontab(minute=0, hour='*/3,8-17') Execute every hour divisible by 3, and every hour during office hours (8am-5pm).
crontab(0, 0, day_of_month='2') Execute on the second day of every month.
crontab(0, 0, day_of_month='2-30/2') Execute on every even numbered day.
crontab(0, 0, day_of_month='1-7,15-21') Execute on the first and third weeks of the month.
crontab(0, 0, day_of_month='11', month_of_year='5') Execute on the eleventh of May every year.
crontab(0, 0, month_of_year='*/3') Execute every day on the first month of every quarter.
"""


# CELERY_CACHE_BACKEND ='default'
# CACHES = {
#     'defaults':{
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'cachedb',
#     }
# }