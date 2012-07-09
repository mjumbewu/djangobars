from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, get_list_or_404
from django.template import RequestContext
from .loader import render_to_string

def render_to_response(*args, **kwargs):
    """
    Returns a HttpResponse whose content is filled with the result of calling
    djangobars.loader.render_to_string() with the passed arguments.
    """
    httpresponse_kwargs = {'content_type': kwargs.pop('mimetype', None)}
    return HttpResponse(render_to_string(*args, **kwargs), **httpresponse_kwargs)

def render(request, *args, **kwargs):
    """
    Returns a HttpResponse whose content is filled with the result of calling
    djangobars.loader.render_to_string() with the passed arguments.
    Uses a RequestContext by default.
    """
    httpresponse_kwargs = {
        'content_type': kwargs.pop('content_type', None),
        'status': kwargs.pop('status', None),
    }

    if 'context_instance' in kwargs:
        context_instance = kwargs.pop('context_instance')
        if kwargs.get('current_app', None):
            raise ValueError('If you provide a context_instance you must '
                             'set its current_app before calling render()')
    else:
        current_app = kwargs.pop('current_app', None)
        context_instance = RequestContext(request, current_app=current_app)

    kwargs['context_instance'] = context_instance

    return HttpResponse(render_to_string(*args, **kwargs),
                        **httpresponse_kwargs)
