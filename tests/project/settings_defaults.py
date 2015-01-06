# Haystack settings for running tests.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'djangobars_tests.db',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'djangobars',
    'project',
]

# Make filepaths relative to settings.
import os.path
def rel_path(*subs):
    root_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(root_path, '..', *subs)

TEMPLATE_DIRS = rel_path('templates'),
#HANDLEBARS_LOADERS = (
#    'djangobars.template.loaders.filesystem.Loader',
#    'djangobars.template.loaders.app_directories.Loader',
#)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

SECRET_KEY = 'testkey'
STATIC_URL = '/static/'
STATICFILES_DIRS = rel_path('static'),
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = ()

SITE_ID = 1
ROOT_URLCONF = 'project.urls'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
