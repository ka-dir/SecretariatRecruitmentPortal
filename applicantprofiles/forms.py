from django.forms import ModelForm
from .models import BioData


class BioDataForm(ModelForm):
    class Meta:
        model = BioData
        fields = '__all__'
