from django.contrib import admin
from jobsite.models import Province, Application, Job, UserApplication


class ProvinceAdmin(admin.ModelAdmin):
    model = Province
    list_display = ['name', 'province_abbr']


class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['company_name', 'description', 'title', 'address_one', 'address_two', 'state']


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ['user_firstname', 'user_lastname', 'user_email', 'user_city', 'user_state', 'job', 'created_on',
                    'cover_letter', 'resume', 'resume_attachment']


class UserApplicationAdmin(admin.ModelAdmin):
    model = UserApplication
    list_display = ['user', 'application']


admin.site.register(Province, ProvinceAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(UserApplication, UserApplicationAdmin)
