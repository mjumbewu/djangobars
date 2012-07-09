from django.test import TestCase, Client, RequestFactory
from djangobars.template import Context
from djangobars.template import Template
from nose.tools import *


class Test_HandlebarsTemplate (TestCase):

    @istest
    def uses_the_helper_functions(self):
        template = Template(u'The URL is: {{ url "blank" }}')
        value = template.render(Context({}))
        assert_equal(value, 'The URL is: /blank_url')
