from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'index.html', context)


def job_list(request):
    context = {}
    return render(request, 'job-list.html', context)


def job_detail(request, pk):
    context = {
        'pk': pk,
    }
    return render(request, 'job-detail.html', context)


def job_create(request):
    context = {}
    return render(request, 'job-create.html', context)


def job_delete(request, pk):
    context = {
        'pk': pk,
    }
    return render(request, 'job-delete.html', context)
