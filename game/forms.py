from django import forms
from . import models

class transaction_form(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ['title','amount', 'description']