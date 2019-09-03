from django.contrib import admin
from jobsite.models import Province, Application, Job, User


class ProvinceAdmin(admin.ModelAdmin):
    model = Province
    list_display = ['name', 'province_abbr']


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'first_name', 'last_name', 'email', 'street', 'city', 'state']


class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['company_name', 'description', 'title', 'address_one', 'address_two', 'state']


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ['user_firstname', 'user_lastname', 'user_email', 'user_city', 'user_state', 'job', 'created_on',
                    'cover_letter', 'resume', 'resume_attachment']


admin.site.register(Province, ProvinceAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
