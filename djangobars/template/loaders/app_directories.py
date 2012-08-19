from django.template.loaders.app_directories import Loader as CoreLoader
from djangobars.template.loader import BaseHandlebarsLoader


class Loader(BaseHandlebarsLoader, CoreLoader):
    pass
