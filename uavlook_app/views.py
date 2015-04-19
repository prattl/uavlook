from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.http import Http404, JsonResponse

from uavlook_app.forms import ContactFormSubmissionForm
from uavlook_app.models import ContactFormSubmission

import threading


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class HomeView(TemplateView):
    template_name = 'uavlook_app/index.html'


class ContactFormAjaxView(View):
    # model = ContactFormSubmission
    # field = '__all__'
    def get(self, request, *args, **kwargs):
        print('Contact Form Ajax GET')
        raise Http404

    def post(self, request, *args, **kwargs):
        print('Contact Form Ajax POST')
        if request.is_ajax():
            print('\tRequest is Ajax')
            success = True
            return JsonResponse({'success': success})
        else:
            raise Http404