from django.shortcuts import render
from .models import Advert
from django.views import generic


# Create your views here.

class VacanciesListView(generic.ListView):
    template_name = 'adverts/vacancies.html.twig'
    context_object_name = 'vacancies_datas'

    def get_queryset(self):
        return Advert.objects.all()


class VacancyDetailView(generic.DetailView):
    template_name = 'adverts/vacancy.html.twig'
    context_object_name = 'vacancy_data'

    def get_queryset(self):
        return Advert.objects.all()
