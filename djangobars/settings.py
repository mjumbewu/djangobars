from django.conf import settings

HANDLEBARS_LOADERS = getattr(settings, 'HANDLEBARS_LOADERS', (
    'djangobars.template.loaders.filesystem.Loader',
    'djangobars.template.loaders.app_directories.Loader',
))

# If not present, HANDLEBARS_DIRS will mimic TEMPLATE_DIRS
if hasattr(settings, 'HANDLEBARS_DIRS'):
    HANDLEBARS_DIRS = settings.HANDLEBARS_DIRS

# If not present, HANDLEBARS_APP_DIRNAME will be 'templates'
if hasattr(settings, 'HANDLEBARS_APP_DIRNAME'):
    HANDLEBARS_APP_DIRNAME = settings.HANDLEBARS_APP_DIRNAME

if hasattr(settings, 'INSTALLED_APPS'):
    INSTALLED_APPS = settings.INSTALLED_APPS
