from django.template.response import TemplateResponse
from .template import HandlebarsTemplate
from .loader import select_template, get_template


class HandlebarsResponse (TemplateResponse):
    def resolve_template(self, template):
        if isinstance(template, (list, tuple)):
            return select_template(template)
        elif isinstance(template, basestring):
            return get_template(template)
        else:
            return template


