from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import GreateJob

@login_required(login_url='../../accounts/login')
def add_view(request):
    if request.method == 'POST':
        new_job = forms.greate_job_form(request.POST)
        if new_job.is_valid():
            new_job = new_job.save(commit=False)
            new_job.owner = request.user
            new_job.save()
            return redirect('confidence:list')
            # return HttpResponse('ثبت شد بابا خفن!')
    form = forms.greate_job_form()
    return render(request, 'add_job.html', {'form':form})

@login_required(login_url='../../accounts/login')
def list_view(request):
    jobs = GreateJob.objects.filter(owner = request.user).order_by('-id')
    jobs.reverse()
    return render(request, 'list_of_jobs.html', {'jobs':jobs, 'name':request.user})


@login_required(login_url='../../accounts/login')
def todays_adds_view(request):
    from datetime import date
    jobs = GreateJob.objects.filter(owner = request.user, date = date.today()).order_by('-date')
    jobs.reverse()
    return render(request, 'list_of_jobs.html', {'jobs':jobs, 'name':request.user})