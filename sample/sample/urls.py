from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?:page1)?$', 'sample.views.page1_view'),
    url(r'^page2$', 'sample.views.page2_view'),
)
