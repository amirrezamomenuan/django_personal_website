from django import forms
from . import models

def all_numeric(pas):
    numbers = "123456789"
    count = 0
    for char in pas:
        if char in numbers:
            count += 1
    if count == len(pas):
        return True
    return False

class signin_form(forms.Form):
    first_name = forms.CharField(max_length=32, min_length=3)
    last_name = forms.CharField(max_length=32, min_length=3)
    username = forms.CharField(max_length=64, min_length=6)
    password1 = forms.CharField(max_length=32, min_length=8)
    password2 = forms.CharField(max_length=32, min_length=8)

    def clean_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password2 != password1:
            error = 'passwords didnt match'
            raise forms.ValidationError(error)
        elif all_numeric(password1):
            error = 'password is all numeric'
            raise forms.ValidationError(error)

    def save(self):
        user = models.User()
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user

from .models import User

class login_form(forms.Form):
    username = forms.CharField(max_length = 64, min_length= 6)
    password = forms.CharField(max_length=32, min_length=8)

    def clean_username(self):
        if not User.objects.filter(username = self.cleaned_data['username']).exists():
            raise forms.ValidationError('user doesnot exist!')

    # def clean_password(self):
    #     if User.objects.filter(username = self.password).exists():
    #         if User.objects.get(username = self.password).password != self.cleaned_data['password']:
    #             raise forms.ValidationError("password is incorrect!")