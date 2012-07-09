from django.template.base import TemplateDoesNotExist
from django.template.loader import find_template
from .template import HandlebarsTemplate

def get_template(template_name):
    """
    Returns a compiled Template object for the given template name,
    handling template inheritance recursively.
    """
    template, origin = find_template(template_name)
    if not hasattr(template, 'render'):
        # template needs to be compiled
        template = get_template_from_string(template, origin, template_name)
    return template

def get_template_from_string(source, origin=None, name=None):
    """
    Returns a compiled Template object for the given template code,
    handling template inheritance recursively.
    """
    return HandlebarsTemplate(source, origin, name)

def select_template(template_name_list):
    "Given a list of template names, returns the first that can be loaded."
    if not template_name_list:
        raise TemplateDoesNotExist("No template names provided")
    not_found = []
    for template_name in template_name_list:
        try:
            return get_template(template_name)
        except TemplateDoesNotExist as e:
            if e.args[0] not in not_found:
                not_found.append(e.args[0])
            continue
    # If we get here, none of the templates could be loaded
    raise TemplateDoesNotExist(', '.join(not_found))
