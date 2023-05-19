from django.urls import path
from .views import BioDataView, BioDataCreateView, BioDataUpdateView

app_name = 'applicantprofiles'

urlpatterns = [
    path('bio-data/', BioDataView.as_view(), name='bio-data'),
    path('bio-data-create/', BioDataCreateView.as_view(), name='bio-data-create'),
    path('bio-data-update/<int:pk>/', BioDataUpdateView.as_view(), name='bio-data-update'),
]
