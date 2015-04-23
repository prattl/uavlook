from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.http import Http404, JsonResponse

from uavlook_app.forms import ContactFormSubmissionForm
from uavlook_app.models import ContactFormSubmission, ContactForm

import json


class HomeView(TemplateView):
    template_name = 'uavlook_app/index.html'


class ContactFormAjaxView(View):
    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        print('Contact Form Ajax POST')
        status = 0
        errors = None
        contact_form = None
        if request.is_ajax():
            print('\tRequest is Ajax')
            try:
                contact_form = ContactForm.objects.get(id=request.POST.get('contact-form-id'))
            except:
                pass
            form = ContactFormSubmissionForm(data=request.POST)
            # if contact_form:
            #     form.contact_form = contact_form
            print('\tForm: %s' % form)
            if form.is_valid():
                print('\tForm is valid.')

                submission = form.save()
                print('\tSubmission is saved.')
                status = 1
            else:
                print('\tForm is invalid.')
                errors = form.errors

            return JsonResponse({
                'status': status,
                'errors': errors,
            })
        else:
            raise Http404