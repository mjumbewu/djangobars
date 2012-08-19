import pybars
from .helpers import _djangobars_


class HandlebarsTemplate (object):
    def __init__(self, template_string, origin=None,
                 name='<Handlebars Template>'):
        c = pybars.Compiler()
        self.handlebars = c.compile(template_string)
        self.name = name
        self.helpers = _djangobars_['helpers'].copy()

    def render(self, context):
        context.render_context.push()
        try:
            s = self.handlebars(
                context, helpers=self.helpers)
            return unicode(s)
        finally:
            context.render_context.pop()
