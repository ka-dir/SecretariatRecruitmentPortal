from django.urls import path
from .views import BioDataView, BioDataCreateView, BioDataUpdateView, AcademicRiderListView, AcademicRiderCreateView, \
    AcademicRiderUpdateView, AcademicRiderDeleteView, ProfessionalRiderListView, ProfessionalRiderCreateView, \
    ProfessionalRiderUpdateView, ProfessionalRiderDeleteView

app_name = 'applicantprofiles'

urlpatterns = [
    # start bio data
    path('bio-data/', BioDataView.as_view(), name='bio-data'),
    path('bio-data-create/', BioDataCreateView.as_view(), name='bio-data-create'),
    path('bio-data-update/<int:pk>/', BioDataUpdateView.as_view(), name='bio-data-update'),
    # end bio data

    # start academic rider
    path('academic-rider', AcademicRiderListView.as_view(), name='academic-rider'),
    path('academic-rider-create/', AcademicRiderCreateView.as_view(), name='academic-rider-create'),
    path('academic-rider-update/<int:pk>/', AcademicRiderUpdateView.as_view(), name='academic-rider-update'),
    path('academic-rider-delete/<int:pk>/', AcademicRiderDeleteView.as_view(), name='academic-rider-delete'),
    # end academic rider

    # start professional rider
    path('professional-rider', ProfessionalRiderListView.as_view(), name='professional-rider'),
    path('professional-rider-create/', ProfessionalRiderCreateView.as_view(), name='professional-rider-create'),
    path('professional-rider-update/<int:pk>/', ProfessionalRiderUpdateView.as_view(),
         name='professional-rider-update'),
    path('professional-rider-delete/<int:pk>/', ProfessionalRiderDeleteView.as_view(), name='professional-rider-delete'),
    # end professional rider

]
