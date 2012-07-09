from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns('',
    url(r'^blank_url$', lambda r: '',
        name='blank'),
#    url(r'^hello$', views.HelloWorld.as_view(),
#        name='hello'),
)
