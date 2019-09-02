from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.db.models import Q

from jobsite.models import Job, Application, User, Province
from jobsite.forms import ApplicationForm, JobForm


# Home page
def index(request):
    context = {}
    return render(request, 'index.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


# List of all jobs
# TODO: make list template
# TODO: support search
def job_list(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, 'job-list.html', context)


# list view for search results
class SearchResultsView(ListView):
    model = Job
    template_name = 'job-search.html'

    # Override built-in get_queryset method to only include search items
    def get_queryset(self):
        query = self.request.GET.get('q')
        jobs = Job.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(company_name__icontains=query)
        )
        return jobs


# Detail of one job by Job pk.
# TODO: make this
def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    context = {
        'job': job,
    }
    return render(request, 'job-detail.html', context)


# Create a new Job.  TODO: move this exclusively to Django admin
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
                state=form.cleaned_data['state'],
            )
            job.save()
            return redirect('job_detail', pk=job.pk)

    context = {
        'form': form
    }
    return render(request, 'job-create.html', context)


# Delete a Job.  For this app, adding and deleting jobs happens in Admin
def job_delete(request, pk):
    job = Job.objects.get(pk=pk)

    context = {
        'job': job,
    }
    return render(request, 'job-delete.html', context)


# Create a new application by User pk
# TODO: make this launchable from particular job page
# TODO: make POST method actually do something
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
