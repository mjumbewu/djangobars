import pybars
from .helpers import _djangobars_


class HandlebarsTemplate (object):
    PARTIALS = {}
    
    def __init__(self, template_string, origin=None,
                 name='<Handlebars Template>',
                 partials=PARTIALS, is_partial=True):
        c = pybars.Compiler()
        self.fn = c.compile(template_string)
        self.name = name
        self.helpers = _djangobars_['helpers'].copy()
        self.partials = partials
        
        if is_partial:
            self.partials[name] = self.fn

    def render(self, context):
        context.render_context.push()
        try:
            s = self.fn(
                context, helpers=self.helpers, partials=self.partials)
            return unicode(s)
        except KeyError, e:
            from djangobars.template.loader import get_template
            partial_name = str(e).strip("'")
            template = get_template(partial_name)
            self.partials[partial_name] = template.fn
            return self.render(context)
        finally:
            context.render_context.pop()
