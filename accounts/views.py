from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import authenticate, login
from .models import User

def signin_view(request):
    if request.method == "POST":
        user = forms.signin_form(request.POST)
        if user.is_valid():
            user = user.save()
            login(request, user)
            if request.POST.get('next'):
                return redirect(request.POST.get('next'))
            return redirect("../../") # ----------------------------------------------------------------------------------

    form = forms.signin_form(request.POST)
    return render(request, 'signin.html', {"form":form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user:
            login(request= request, user= user)
            return redirect('../../')
    form  = forms.login_form()
    return render(request, 'login.html', {'form':form})
