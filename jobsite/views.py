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
# TODO: make POST method actually do something
def application_create(request, pk):
    user = request.user
    form = ApplicationForm()

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job = Job.objects.get(pk=pk)
            application = Application(
                user_firstname=form.cleaned_data['user_firstname'],
                user_lastname=form.cleaned_data['user_lastname'],
                user_email=form.cleaned_data['user_email'],
                user_city=form.cleaned_data['user_city'],
                user_state=form.cleaned_data['user_state'],
                job=job,
                cover_letter=form.cleaned_data['cover_letter'],
                resume=form.cleaned_data['resume'],
                resume_attachment=request.FILES.get('resume_attachment'),
            )
            application.save()

            return redirect('job_detail', pk=job.pk)

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
