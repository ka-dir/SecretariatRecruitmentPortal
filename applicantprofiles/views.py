from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import BioDataForm, AcademicRiderForm, ProfessionalRiderForm
from .models import BioData, AcademicQualification, ProfessionalQualification


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


# Academic Rider Create
class AcademicRiderCreateView(generic.CreateView):
    template_name = 'applicantprofiles/academic-rider-create.html.twig'
    form_class = AcademicRiderForm

    def get_success_url(self):
        return reverse('applicantprofiles:academic-rider')


# Academic Rider List
class AcademicRiderListView(generic.ListView):
    template_name = 'applicantprofiles/academic-rider.html.twig'
    context_object_name = 'academic_datas'

    def get_queryset(self):
        return AcademicQualification.objects.all()


# Academic Rider Update
class AcademicRiderUpdateView(generic.UpdateView):
    template_name = 'applicantprofiles/academic-rider-update.html.twig'
    form_class = AcademicRiderForm

    def get_queryset(self):
        return AcademicQualification.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:academic-rider')


# Academic Rider Delete
class AcademicRiderDeleteView(generic.DeleteView):
    template_name = 'applicantprofiles/academic-rider-delete.html.twig'

    def get_queryset(self):
        return AcademicQualification.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:academic-rider')


# Professional Rider List
class ProfessionalRiderListView(generic.ListView):
    template_name = 'applicantprofiles/professional-rider.html.twig'
    context_object_name = 'professional_datas'

    def get_queryset(self):
        return ProfessionalQualification.objects.all()


# Professional Rider Create
class ProfessionalRiderCreateView(generic.CreateView):
    template_name = 'applicantprofiles/professional-rider-create.html.twig'
    form_class = ProfessionalRiderForm

    def get_success_url(self):
        return reverse('applicantprofiles:professional-rider')


# Professional Rider Update
class ProfessionalRiderUpdateView(generic.UpdateView):
    template_name = 'applicantprofiles/professional-rider-update.html.twig'
    form_class = ProfessionalRiderForm

    def get_queryset(self):
        return ProfessionalQualification.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:professional-rider')

# Professional Rider Delete
class ProfessionalRiderDeleteView(generic.DeleteView):
    template_name = 'applicantprofiles/professional-rider-delete.html.twig'

    def get_queryset(self):
        return ProfessionalQualification.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:professional-rider')
