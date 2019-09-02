from django.shortcuts import render


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


# Detail of one job by Job pk
def job_detail(request, pk):
    context = {
        'pk': pk,
    }
    return render(request, 'job-detail.html', context)


# Create a new Job
def job_create(request):
    context = {}
    return render(request, 'job-create.html', context)


# Delete a Job
def job_delete(request, pk):
    context = {
        'pk': pk,
    }
    return render(request, 'job-delete.html', context)


# Create a new application by User pk
def application_create(request):
    context = {
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
