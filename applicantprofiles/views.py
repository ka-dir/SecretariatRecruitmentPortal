from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import BioDataForm
from .models import BioData


# Create your views here.




# Create BioData
class BioDataCreateView(generic.CreateView):
    template_name = 'applicantprofiles/bio-data-create.html.twig'
    form_class = BioDataForm

    def get_success_url(self):
        return reverse('applicantprofiles:bio-data')


# BioData TemplateView

class BioDataView(generic.ListView):
    template_name = 'applicantprofiles/bio-data.html.twig'
    context_object_name = 'bio_datas'

    def get_queryset(self):
        return BioData.objects.all()


# Update BioData

class BioDataUpdateView(generic.UpdateView):
    template_name = 'applicantprofiles/bio-data-update.html.twig'
    form_class = BioDataForm

    def get_queryset(self):
        return BioData.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:bio-data')
