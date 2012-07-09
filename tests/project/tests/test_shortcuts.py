from django.test import TestCase, Client, RequestFactory
from django.template import Context
from djangobars.shortcuts import render, render_to_response
from nose.tools import *


class Test_renderToResponse (TestCase):

    @istest
    def renders_simple_hello_world(self):
        response = render_to_response(template_name="hello1.txt")
        assert_equal(response.content, 'Hello, World!\n')

    @istest
    def renders_simple_greeting_with_one_variable(self):
        context = Context({'name': 'Mjumbe'})
        response = render_to_response(template_name="hello2.txt",
                                      context_instance=context)
        assert_equal(response.content, 'Hello, Mjumbe!\n')


class Test_render (TestCase):

    def setUp(self):
        from django.contrib.auth.models import User
        user = User(username='mjumbewu',
                    email='mjumbewu@example.com',
                    first_name="Mjumbe")
        user.save()

        self.request = RequestFactory()
        self.request.user = user

    @istest
    def uses_request_context_variables(self):
        response = render(self.request, template_name="hello3.txt")
        assert_equal(response.content, 'Hello, Mjumbe!\n')
