from django.forms import ModelForm
from .models import BioData, AcademicQualification, ProfessionalQualification, RelevantCourse, \
    MembershipProfessionalBody, ProfessionalExperience, Reference


class BioDataForm(ModelForm):
    class Meta:
        model = BioData
        fields = '__all__'


class AcademicRiderForm(ModelForm):
    class Meta:
        model = AcademicQualification
        fields = '__all__'


class ProfessionalRiderForm(ModelForm):
    class Meta:
        model = ProfessionalQualification
        fields = '__all__'


class RelevantCourseForm(ModelForm):
    class Meta:
        model = RelevantCourse
        fields = '__all__'


class MembershipProfessionalBodyForm(ModelForm):
    class Meta:
        model = MembershipProfessionalBody
        fields = '__all__'


class ProfessionalExperienceForm(ModelForm):
    class Meta:
        model = ProfessionalExperience
        fields = '__all__'


class ReferenceForm(ModelForm):
    class Meta:
        model = Reference
        fields = '__all__'
