from django.conf.urls import patterns, include, url

import test_app

urlpatterns = patterns('',
    url(r'^', include('test_app.urls')),
)
