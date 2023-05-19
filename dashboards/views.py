from django.shortcuts import render
from django.views import generic


# Create your views here.

class DashboardView(generic.TemplateView):
    template_name = 'dashboards/dashboard.html.twig'
