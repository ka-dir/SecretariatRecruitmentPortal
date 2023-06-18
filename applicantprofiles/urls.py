from django.urls import path
from .views import BioDataView, BioDataCreateView, BioDataUpdateView, AcademicRiderListView, AcademicRiderCreateView, \
    AcademicRiderUpdateView, AcademicRiderDeleteView, ProfessionalRiderListView, ProfessionalRiderCreateView, \
    ProfessionalRiderUpdateView, ProfessionalRiderDeleteView, CoursesTrainingListView, CoursesTrainingCreateView, \
    CoursesTrainingUpdateView, CoursesTrainingDeleteView, MembershipListView, MembershipCreateView, \
    MembershipUpdateView, MembershipDeleteView, EmploymentHistoryListView, EmploymentHistoryCreateView, \
    EmploymentHistoryUpdateView, EmploymentHistoryDeleteView, RefereeListView, RefereeCreateView, RefereeUpdateView, \
    RefereeDeleteView

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
    path('professional-rider-delete/<int:pk>/', ProfessionalRiderDeleteView.as_view(),
         name='professional-rider-delete'),
    # end professional rider

    # start Courses/Training
    path('courses-training', CoursesTrainingListView.as_view(), name='courses-training'),
    path('courses-training-create/', CoursesTrainingCreateView.as_view(), name='courses-training-create'),
    path('courses-training-update/<int:pk>/', CoursesTrainingUpdateView.as_view(),
         name='courses-training-update'),
    path('courses-training-delete/<int:pk>/', CoursesTrainingDeleteView.as_view(),
         name='courses-training-delete'),
    # end Courses/Training

    # start Membership
    path('membership', MembershipListView.as_view(), name='membership'),
    path('membership-create/', MembershipCreateView.as_view(), name='membership-create'),
    path('membership-update/<int:pk>/', MembershipUpdateView.as_view(),
         name='membership-update'),
    path('membership-delete/<int:pk>/', MembershipDeleteView.as_view(),
         name='membership-delete'),
    # end Membership

    # start employment
    path('employment-history', EmploymentHistoryListView.as_view(), name='employment-history'),
    path('employment-history-create', EmploymentHistoryCreateView.as_view(), name='employment-history-create'),
    path('employment-history-update/<int:pk>/', EmploymentHistoryUpdateView.as_view(),
         name='employment-history-update'),
    path('employment-history-delete/<int:pk>/', EmploymentHistoryDeleteView.as_view(),
         name='employment-history-delete'),
    # end employment

    # start referee
    path('referee', RefereeListView.as_view(), name='referee'),
    path('referee-create', RefereeCreateView.as_view(), name='referee-create'),
    path('referee-update/<int:pk>/', RefereeUpdateView.as_view(), name='referee-update'),
    path('referee-delete/<int:pk>/', RefereeDeleteView.as_view(), name='referee-delete'),

    # end referee

]
