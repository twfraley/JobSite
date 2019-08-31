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

from jobsite.views import index, job_list, job_create, job_delete, job_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('job-list/', job_list, name='job_list'),
    path('job-detail/<int:pk>/', job_detail, name='job_detail'),
    path('job-create/', job_create, name='job_create'),
    path('job-delete/<int:pk>/', job_delete, name='job_delete'),
]
