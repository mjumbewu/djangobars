from django.template import Node, Variable, TemplateSyntaxError, Library, Context
from ..template.loader import get_template

register = Library()


class IncludeHandlebarsNode (Node):
    def __init__(self, name, inner_context=None):
        self.name = Variable(name)
        self.inner_context = None if inner_context is None else Variable(inner_context)

    def render(self, context):
        name = self.name.resolve(context)
        template = get_template(name)
        if self.inner_context is None:
            inner_context = context
        else:
            inner_context = self.inner_context.resolve(context)
        return template.render(inner_context)


@register.tag
def include_handlebars(parser, token):
    """
    Include a Handlebars template processed with the current context.

    """
    bits = token.contents.split()
    if len(bits) not in (2, 3):
        raise TemplateSyntaxError(
            "'include_handlebars' tag takes one or two arguments: the name/id "
            "of the template to include and, optionally, a new context.")
    return IncludeHandlebarsNode(*bits[1:])
