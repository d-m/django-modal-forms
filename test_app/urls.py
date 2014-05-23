from django.conf.urls import patterns, include, url

from .views import HomeView, TestFormView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^test-form/$', TestFormView.as_view(), name="test-form"),
)
