import pybars


class HandlebarsTemplate (object):
    def __init__(self, template_string, origin=None, name='<Handlebars Template>'):
        self.handlebars = pybars.Compiler().compile(template_string)
        self.name = name

    def render(self, context):
        context.render_context.push()
        try:
            return unicode(self.handlebars(context))
        finally:
            context.render_context.pop()


