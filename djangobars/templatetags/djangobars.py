from django.template import Node, Variable, TemplateSyntaxError, Library
from ..template.loader import get_template

register = Library()


class IncludeHandlebarsNode (Node):
    def __init__(self, name):
        self.name = Variable(name)

    def render(self, context):
        name = self.name.resolve(context)
        template = get_template(name)
        return template.render(context)


@register.tag
def include_handlebars(parser, token):
    """
    Include a Handlebars template processed with the current context.

    """
    bits = token.contents.split()
    if len(bits) != 2:
        raise TemplateSyntaxError(
            "'include_handlebars' tag takes one argument: the name/id of "
            "the template to include.")
    return IncludeHandlebarsNode(*bits[1:])
