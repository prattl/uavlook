from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'uavlook_app/index.html'



