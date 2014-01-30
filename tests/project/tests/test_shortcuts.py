from django.test import TestCase, Client, RequestFactory
from djangobars.template import Context
from djangobars.shortcuts import render, render_to_response
from nose.tools import *


class Test_renderToResponse (TestCase):

    @istest
    def renders_simple_hello_world(self):
        response = render_to_response(template_name="hello1.txt")
        assert_equal(response.content, ('Hello, World!\n').encode())

    @istest
    def renders_simple_greeting_with_one_variable(self):
        context = Context({'name': 'Mjumbe'})
        response = render_to_response(template_name="hello2.txt",
                                      context_instance=context)
        assert_equal(response.content, ('Hello, Mjumbe!\n').encode())

    @istest
    def renders_simple_greeting_with_partial(self):
        context = Context({'name': 'Mjumbe'})
        response = render_to_response(template_name="hello5.txt",
                                      context_instance=context)
        assert_equal(response.content, ('Hello, Mjumbe, nice to meet you!\n').encode())


class Test_render (TestCase):

    def setUp(self):
        from django.contrib.auth.models import User
        user = User(username='mjumbewu',
                    email='mjumbewu@example.com',
                    first_name="Mjumbe")
        user.save()

        self.request = RequestFactory()
        self.request.user = user

    def tearDown(self):
        from django.contrib.auth.models import User
        User.objects.all().delete()

    @istest
    def uses_request_context_variables(self):
        response = render(self.request, template_name="hello3.txt")
        assert_equal(response.content, ('Hello, mjumbewu!\n').encode())

    @istest
    def uses_helper_functions(self):
        response = render(self.request, template_name="hello4.txt")
        assert_equal(response.content, ('Hello, mjumbewu, go to /blank_url!\n').encode())
