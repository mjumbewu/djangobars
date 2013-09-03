# Django settings for sample project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sample.db',
    }
}

# Time
TIME_ZONE = 'America/Chicago'
USE_TZ = True

# L10n
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

STATIC_URL = '/static/'

# Templates
JSTEMPLATE_APP_DIRNAMES = HANDLEBARS_APP_DIRNAMES = (
    'handlebars',
)

ROOT_URLCONF = 'sample.urls'
WSGI_APPLICATION = 'sample.wsgi.application'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)
SECRET_KEY = 'nu9(ryx8)=mji%65ywrjx)755vf@pgrrs(cffn5g%&y%l_7lr!'
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.staticfiles',

    'jstemplate',
    'djangobars',

    'sample',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
