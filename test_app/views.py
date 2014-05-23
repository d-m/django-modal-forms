import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import TestForm


class HomeView(TemplateView):
    template_name = 'test_app/home.html'


class AjaxTemplateMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)


class TestFormView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'test_app/test_form.html'
    form_class = TestForm
    success_url = reverse_lazy('home')
    success_message = "Way to go!"
