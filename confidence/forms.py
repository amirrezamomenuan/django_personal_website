from django import forms
from .models import GreateJob

class greate_job_form(forms.ModelForm):
    class Meta:
        model = GreateJob
        fields = ['job']