import pybars
from .helpers import _djangobars_

try:
    strtype = unicode
except NameError:
    strtype = str

class FakeError(Exception):
    pass

try:
    from pybars import PybarsError
except ImportError:
    PybarsError = FakeError


class PartialList():
    """
    If the code references a partial in the template directory, then
    load and render the template
    """
    partials = None

    def __init__(self, partials=None):
        if partials is not None:
            self.partials = partials
        else:
            self.partials = {}

    def __contains__(self, key):
        return self.get(key) is not None

    def __getitem__(self, partial_name):
        if partial_name not in self.partials:
            from djangobars.template.loader import get_template
            template = get_template(partial_name)
            if template:
                self.partials[partial_name] = template.fn
        return self.partials.get(partial_name)

    def get(self, partial_name, default=None):
        try: return self[partial_name]
        except KeyError: return default

    def __setitem__(self, key, val):
        self.partials[key] = val


class HandlebarsTemplate(object):
    PARTIALS = {}

    def __init__(self, template_string, origin=None,
                 name='<Handlebars Template>',
                 partials=PARTIALS, is_partial=True):
        c = pybars.Compiler()
        self.fn = c.compile(template_string)
        self.name = name
        self.helpers = _djangobars_['helpers'].copy()
        self.partials = PartialList(partials)

        if is_partial:
            self.partials[name] = self.fn

    def _compile_partial(self, partial_name):
        from djangobars.template.loader import get_template
        template = get_template(partial_name)
        self.partials[partial_name] = template.fn

    def render(self, context):
        if hasattr(context, 'render_context'):
            context.render_context.push()

        try:
            s = self.fn(
                context, helpers=self.helpers, partials=self.partials)
            return strtype(s)
        except KeyError as e:
            partial_name = strtype(e).strip("'")
            self._compile_partial(partial_name)
            return self.render(context)
        except PybarsError as e:
            #support for Pybars 0.8+
            err = e.message
            if err.startswith('Partial') and err.find('not defined'):
                partial_name = err[err.index('"')+1:err.rindex('"')]
                self._compile_partial(partial_name)
                return self.render(context)
            else:
                raise
        finally:
            if hasattr(context, 'render_context'):
                context.render_context.pop()
