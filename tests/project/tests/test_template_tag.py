from django.test import TestCase, Client, RequestFactory
from django.template import Context
from django.template import Template
from nose.tools import *


class Test_IncludeTemplateTag (TestCase):

    @istest
    def renders_a_template_without_variables(self):
        template = Template(u'{% load djangobars %}This is a Django template.  Handlebars is like: "{% include_handlebars "hello1.txt" %}".')
        value = template.render(Context({}))
        assert_equal(value, 'This is a Django template.  Handlebars is like: "Hello, World!\n".')

    @istest
    def renders_a_template_with_variables(self):
        template = Template(u'{% load djangobars %}This is a Django template.  Handlebars is like: "{% include_handlebars "hello2.txt" %}".')
        value = template.render(Context({'name': 'Mjumbe'}))
        assert_equal(value, 'This is a Django template.  Handlebars is like: "Hello, Mjumbe!\n".')

    @istest
    def renders_a_template_with_a_nested_context(self):
        template = Template(u'{% load djangobars %}This is a Django template.  Handlebars is like: "{% include_handlebars "hello2.txt" data %}".')
        value = template.render(Context({'data': {'name': 'Mjumbe'}}))
        assert_equal(value, 'This is a Django template.  Handlebars is like: "Hello, Mjumbe!\n".')

    @istest
    def renders_a_template_with_a_non_dict_nested_context(self):
        template = Template(u'{% load djangobars %}This is a Django template.  Handlebars is like: "{% include_handlebars "hello8.txt" data %}".')
        value = template.render(Context({'data': 'Mjumbe'}))
        assert_equal(value, 'This is a Django template.  Handlebars is like: "Hello, Mjumbe!\n".')

    @istest
    def renders_a_template_with_helper_functions(self):
        template = Template(u'{% load djangobars %}This is a Django template.  Handlebars is like: "{% include_handlebars "hello4.txt" %}".')
        value = template.render(Context({'user': 'Mjumbe'}))
        assert_equal(value, 'This is a Django template.  Handlebars is like: "Hello, Mjumbe, go to /blank_url!\n".')

    @istest
    def renders_from_app_folders(self):
        template = Template(u'{% load djangobars %}This is a Django template.  Handlebars is like: "{% include_handlebars "hello6.txt" %}".')
        value = template.render(Context({}))
        assert_equal(value, 'This is a Django template.  Handlebars is like: "Hello, World!\n".')
