import os
import sys

from django.core.exceptions import ImproperlyConfigured
from django.template.loaders.app_directories import Loader as CoreLoader
from django.utils.importlib import import_module
from djangobars.template.loader import BaseHandlebarsLoader
from ... import settings


# At compile time, cache the directories to search.
fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()
app_template_dirs = []
app_dir_names = getattr(settings, 'HANDLEBARS_APP_DIRNAMES', 'templates')

for app in settings.INSTALLED_APPS:
    try:
        mod = import_module(app)
    except ImportError as e:
        raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))

    for app_dir_name in app_dir_names:
        try:
            template_dir = os.path.join(os.path.dirname(mod.__file__), app_dir_name)
        except AttributeError as e:
            raise ImproperlyConfigured('HANDLEBARS_APP_DIRNAMES must be a collection of strings, not %r' % (app_dir_names,))

        if os.path.isdir(template_dir):
            if hasattr(template_dir, 'decode'):
                # Python 2
                template_dir = template_dir.decode(fs_encoding)
            app_template_dirs.append(template_dir)

# It won't change, so convert it to a tuple to save memory.
app_template_dirs = tuple(app_template_dirs)

class Loader(BaseHandlebarsLoader, CoreLoader):

    def get_template_sources(self, template_name, template_dirs=None):
        """
        Returns the absolute paths to "template_name", when appended to each
        directory in "template_dirs". Any paths that don't lie inside one of the
        template dirs are excluded from the result set, for security reasons.
        """

        if template_dirs is None:
            template_dirs = app_template_dirs

        return super(Loader, self).get_template_sources(template_name, template_dirs=template_dirs)
