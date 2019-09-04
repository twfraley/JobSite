"""RecruitRooster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include

from jobsite.views import index, job_list, job_detail, application_create, \
    application_detail, application_list, SearchResultsView, SignUp

# Typically would spread URL files into each namespace, but not needed with a small app like this
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUp.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('job-list/', job_list, name='job_list'),
    path('job-search/', SearchResultsView.as_view(), name='job_search'),
    path('job-detail/<int:pk>/', job_detail, name='job_detail'),
    path('application-create/<int:pk>/', application_create, name='application_create'),
    path('application-list/', application_list, name='application_list'),
    path('application-detail/<int:pk>/', application_detail, name='application_detail'),
]
