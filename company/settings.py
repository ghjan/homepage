# coding:utf-8
import os

DEBUG = False

IS_BAE_ENV = False

UPLOAD_LOCATION = '/static/upload/'

# 是否记录日志启动logging
LOGGING = False
# 管理员邮箱
ADMIN_EMAIL = 'cajan2@163.com'

ADMINS = (
    ('David Zhang', 'cajan2@163.com'),
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

WEB_NAME = '艾易软件-POS,ERP,进销存,workflow,HR,DRP 业务开发平台'

# ====管理端pagesize 设定===================
ARTICLE_PAGE_SIZE = 20
PHOTO_PAGE_SIZE = 18
# ====前端 pagesize 设定====================
FRONT_ARTICLE_PAGE_SIZE = 15
FRONT_PHOTO_PAGE_SIZE = 20
FRONT_JOKE_PAGE_SIZE = 15

MANAGERS = ADMINS

MYNET_PAGE_SIZE = 15
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'company',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3308',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static/upload/').replace('\\', '/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"


STATIC_ROOT = '/data/media/homepage/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
# STATICFILES_DIRS = (
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
#     ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
#     ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
#     ('img', os.path.join(STATIC_ROOT, 'img').replace('\\', '/')),
#     ('flash', os.path.join(STATIC_ROOT, 'flash').replace('\\', '/')),
# )

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$wow23efger46yutiuefgg;abcd@j*2w23wcll+x_&amp;l4c!25hasee2+*sibdk'

ROOT_URLCONF = 'company.urls'

# Python dotted path to the WSGI application used by Django's runserver.
# WSGI_APPLICATION = 'yihaomen.wsgi.application'


try:
    from settings_local import *
except:
    pass

# middleware
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.sites',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',

    'company',
    'app',

    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration.
# more details on how to customize your logging configuration
# See https://docs.djangoproject.com/en/1.8/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'include_html': True,
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'info_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/info.log',
            'formatter': 'verbose',
        },
        'error_handler': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
            'formatter': 'verbose',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['info_handler', 'error_handler'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'real.views': {
            'handlers': ['error_handler', 'mail_admins'],
            'level': 'INFO',
        },
    }
}
