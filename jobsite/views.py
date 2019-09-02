from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from jobsite.models import Job, Application, User, Provence
from jobsite.forms import ApplicationForm, JobForm


# Home page
def index(request):
    context = {}
    return render(request, 'index.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


# List of all jobs
# TODO: support search
def job_list(request):
    context = {}
    return render(request, 'job-list.html', context)


# Detail of one job by Job pk.  Also supports job delete
def job_detail(request, pk):
    job = Job.objects.get(pk=pk)

    if request.method == 'DELETE':
        job.objects.delete(pk=pk)
        return HttpResponseRedirect('job_list')

    context = {
        'job': job,
    }
    return render(request, 'job-detail.html', context)


# Create a new Job
def job_create(request):
    form = JobForm()

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = Job(
                company_name=form.cleaned_data['company_name'],
                description=form.cleaned_data['description'],
                title=form.cleaned_data['title'],
                address_one=form.cleaned_data['address_one'],
                address_two=form.cleaned_data['address_two'],
                state=form.cleaned_data['state'],
            )
            job.save()
            return redirect('job_detail', pk=job.pk)

    context = {
        'form': form
    }
    return render(request, 'job-create.html', context)


# Delete a Job.  Deprecated. TODO: clean this up
def job_delete(request, pk):
    job = Job.objects.get(pk=pk)

    context = {
        'job': job,
    }
    return render(request, 'job-delete.html', context)


# Create a new application by User pk
def application_create(request, pk):
    user = request.user
    form = ApplicationForm()

    if request.method == 'POST':
        pass

    context = {
        'form': form,
        'user': user,
        'pk': pk
    }
    return render(request, 'application-create.html', context)


# List applications by User pk
def application_list(request):
    context = {
    }
    return render(request, 'application-list.html', context)


# View detail by application pk
def application_detail(request):
    context = {
    }
    return render(request, 'application-detail.html', context)
