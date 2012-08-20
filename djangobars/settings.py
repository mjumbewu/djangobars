from django.conf import settings

HANDLEBARS_LOADERS = getattr(settings, 'HANDLEBARS_LOADERS', (
    'djangobars.template.loaders.filesystem.Loader',
    'djangobars.template.loaders.app_directories.Loader',
))

# A value of None should make HANDLEBARS_DIRS mimic TEMPLATE_DIRS
HANDLEBARS_DIRS = getattr(settings, 'HANDLEBARS_DIRS', None)
