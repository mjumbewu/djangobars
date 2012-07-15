djangobars
==========

An extension to allow Django to use Handlebars templates through the pybars port of Handlebars.js

Because don't we all want to use the same templates on the client that we do on the server?

Installation
------------

1. ``pip install djangobars``

2. Add ``'djangobars'`` to your installed applications.

3. Add a ``HANDLEBARS_LOADERS`` value to your settings module.  You will probably
   want::

       HANDLEBARS_LOADERS = (
           'djangobars.template.loaders.filesystem.Loader',
           'djangobars.template.loaders.app_directories.Loader',
       )

4. *(optional)* Add a ``HANDLEBARS_DIRS`` value to your setting module.  By default,
   djangobars will search in your ``TEMPLATE_DIRS`` folder, but you can use the
   ``HANDLEBARS_DIRS`` value to override this behavior.


Usage
-----

Use pretty much just as you would Django's own built-in templates.  Instead of::

    from django.shortcuts import render

    def my_view(request):
        # View code here...
        return render(request, 'myapp/index.html', {"foo": "bar"},
            content_type="application/xhtml+xml")

do this::

    from djangobars.shortcuts import render

    def my_view(request):
        # View code here...
        return render(request, 'myapp/handlebar_index.html', {"foo": "bar"},
            content_type="application/xhtml+xml")

And instead of::

    from django.views.generic import TemplateView

    class MyView (TemplateView):
        template_name = 'myapp/index.html'

do this::

    from django.views.generic import TemplateView
    from djangobars.resonse import HandlebarsResponse

    class MyView (TemplateView):
        template_name = 'myapp/handlebar_index.html'
        response_class = HandlebarsResponse
