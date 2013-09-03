Unifying Back-/Front-end Templates in Django
============================================

This sample uses the following libraries:

- **Django apps**:

  * djangobars (pybars + Django tags)
  * django-jstemplates

- **JavaScript libraries**:

  * jquery
  * handlebars.js
  * backbone.js (and underscore.js)
  * backbone.marrionette.js (though it's completely extra, and if you're not
    familiar with Backbone, I'd recommend against using Marrionette)

The *pybars* repo from @wbond (https://github.com/wbond/pybars) appears to be
more up to date than the original on PyPI, and it's compatible with Python 3.3.
Use that one.

Originally I aimed to have a drop-in replacement for the Django templating
system with Djangobars. However, that's not really what I wanted. I wanted to
keep my back-end and front-end templates DRY. The Django template language is
quite fine for what it is, and I really have no need to use a different
template language in many cases. It is really only those things that I'll be
rendering with JavaScript that I need to use another template language for.

I'm using Handlebars because it's available in both JavaScript and Python.
Mustache has a more active, mature implementation in Python, but I find it to
be limiting. Handlebars is just the right amount of logiclessness.

* Use Django templates for portions of of the interface that will never change
  once rendered.
* Use Handlebars for everything else.
* Use Django REST Framework serializers to unify the data interfaces.

For this sample, I'm just going to build a couple of panels that toggle back
and forth between each other.

------------------------------------------------------------

Setup
-----

In *settings.py*, add both set the ``JSTEMPLATE_APP_DIRNAMES`` to the same name as the
name for the templates app. This is most likely::

	JSTEMPLATE_APP_DIRNAMES = HANDLEBARS_APP_DIRNAME = (
	    'handlebars',
	)

In your app directory, create folders named *templates* and *handlebars*. The
former is for your Django templates.

Create a base Django template, just as you normally might, for those things
that are common across templates.

If you choose to use bower straight from the command line (e.g., without the
aid of an app like *django-bower*), then remember to set up your *.bowerrc*
file to install your components into the right place.


Rendering Handlebars templates with Djangobars
----------------------------------------------

Rendering your Handlebars templates from within your Django templates is super
simple. Just load the template helper at the beginning of your template::

	{% extends 'djangobars_sample/base.html' %}
	{% load include_handlebars from djangobars %}
	...

And then use the ``include_handlebars`` tag much as you would the ``include``
Django tag::

	{% include_handlebars 'page1-tpl.html' %}

Things to remember about the Handlebars templates:

* Refrain from putting ``<script>`` tags in the templates. This will confilict
  with the way the templates are handled on the javascript side. you'll end up
  with something like::

        <script type="template/x-handlebars" id="my-buggy-tpl">
          This is the beginning of my template.
          
          <script>
          	do('something');
          </script> <!-- This closing script tag is going to cause you headaches -->

          This is the end of my template.
        </script>

  Instead, put your scripts in a django template and use the
  ``{% include_handlebars %}`` tag.


Bootstrapping data
------------------

With Backbone, I often hook my models and collections straight up to my Django
REST Framework endpoints. However, to save a roundtrip and simplify some
potential asynchronous headaches of dealing with page state before data has
arrived, I end up bootstrapping data (i.e., rendering JSON representations of
data directly into the page on the server). To do this I take advantage of 
DRF's decoupled serializers.

This happens especially often with user data. When bootstrapping user data into
the page, always take care to use a custom serializer, as you don't want all of
the user's data getting sent down.


Limitations
-----------

* If you want to use custom Handlebars helpers, you'll have to implement them
  in both Python and JavaScript
