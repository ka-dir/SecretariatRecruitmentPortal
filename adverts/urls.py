from django.urls import path
from .views import VacanciesListView, VacancyDetailView

app_name = 'adverts'

urlpatterns = [
    path('vacancies', VacanciesListView.as_view(), name='vacancies'),
    path('vacancy/<str:pk>/', VacancyDetailView.as_view(), name="vacancy"),
]
