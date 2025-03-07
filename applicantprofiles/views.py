from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import BioDataForm, AcademicRiderForm, ProfessionalRiderForm, RelevantCourseForm, \
    MembershipProfessionalBodyForm, ProfessionalExperienceForm, ReferenceForm
from .models import BioData, AcademicQualification, ProfessionalQualification, RelevantCourse, \
    MembershipProfessionalBody, MembershipProfessionalBody, ProfessionalExperience, Reference


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


# Courses/Training  List
class CoursesTrainingListView(generic.ListView):
    template_name = 'applicantprofiles/courses-training.html.twig'
    context_object_name = 'courses_training_datas'

    def get_queryset(self):
        return RelevantCourse.objects.all()


# Courses/Training   Create
class CoursesTrainingCreateView(generic.CreateView):
    template_name = 'applicantprofiles/courses-training-create.html.twig'
    form_class = RelevantCourseForm

    def get_success_url(self):
        return reverse('applicantprofiles:courses-training')


# Courses/Training  Update
class CoursesTrainingUpdateView(generic.UpdateView):
    template_name = 'applicantprofiles/courses-training-update.html.twig'
    form_class = RelevantCourseForm

    def get_queryset(self):
        return RelevantCourse.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:courses-training')


# Courses/Training  Delete
class CoursesTrainingDeleteView(generic.DeleteView):
    template_name = 'applicantprofiles/courses-training-delete.html.twig'

    def get_queryset(self):
        return RelevantCourse.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:courses-training')


# Membership  List
class MembershipListView(generic.ListView):
    template_name = 'applicantprofiles/membership.html.twig'
    context_object_name = 'membership_datas'

    def get_queryset(self):
        return MembershipProfessionalBody.objects.all()


# Membership  Create
class MembershipCreateView(generic.CreateView):
    template_name = 'applicantprofiles/courses-training-create.html.twig'
    form_class = MembershipProfessionalBodyForm

    def get_success_url(self):
        return reverse('applicantprofiles:membership')


# Membership Update
class MembershipUpdateView(generic.UpdateView):
    template_name = 'applicantprofiles/membership-update.html.twig'
    form_class = MembershipProfessionalBodyForm

    def get_queryset(self):
        return MembershipProfessionalBody.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:membership')


# Membership Delete
class MembershipDeleteView(generic.DeleteView):
    template_name = 'applicantprofiles/membership-delete.html.twig'

    def get_queryset(self):
        return MembershipProfessionalBody.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:membership')


class EmploymentHistoryListView(generic.ListView):
    template_name = 'applicantprofiles/employment-history.html.twig'
    context_object_name = 'employee_history_datas'

    def get_queryset(self):
        return ProfessionalExperience.objects.all()


class EmploymentHistoryCreateView(generic.CreateView):
    template_name = 'applicantprofiles/employment-history-create.html.twig'
    form_class = ProfessionalExperienceForm

    def get_success_url(self):
        return reverse('applicantprofiles:employment-history')


class EmploymentHistoryUpdateView(generic.UpdateView):
    template_name = 'applicantprofiles/employment-history-update.html.twig'
    form_class = ProfessionalExperienceForm

    def get_queryset(self):
        return ProfessionalExperience.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:employment-history')


class EmploymentHistoryDeleteView(generic.DeleteView):
    template_name = 'applicantprofiles/employment-history-delete.html.twig'

    def get_queryset(self):
        return ProfessionalExperience.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:employment-history')


class RefereeListView(generic.ListView):
    template_name = 'applicantprofiles/referee.html.twig'
    context_object_name = 'referee_datas'

    def get_queryset(self):
        return Reference.objects.all()


class RefereeCreateView(generic.CreateView):
    template_name = 'applicantprofiles/referee-create.html.twig'
    form_class = ReferenceForm

    def get_success_url(self):
        return reverse('applicantprofiles:referee')


class RefereeUpdateView(generic.UpdateView):
    template_name = 'applicantprofiles/referee-update.html.twig'
    form_class = ReferenceForm

    def get_queryset(self):
        return Reference.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:referee')


class RefereeDeleteView(generic.DeleteView):
    template_name = 'applicantprofiles/referee-delete.html.twig'

    def get_queryset(self):
        return Reference.objects.all()

    def get_success_url(self):
        return reverse('applicantprofiles:referee')



