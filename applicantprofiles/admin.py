from django.contrib import admin
from .models import BioData, AcademicQualification, CriminalOffence, ProfessionalQualification, RelevantCourse, \
    MembershipProfessionalBody, ProfessionalExperience, Reference

# Register your models here.
admin.site.register(BioData)
admin.site.register(AcademicQualification)
admin.site.register(CriminalOffence)
admin.site.register(ProfessionalQualification)
admin.site.register(RelevantCourse)
admin.site.register(MembershipProfessionalBody)
admin.site.register(ProfessionalExperience)
admin.site.register(Reference)
