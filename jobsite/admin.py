from django.contrib import admin
from jobsite.models import Provence, Application, Job, User


class ProvenceAdmin(admin.ModelAdmin):
    model = Provence
    list_display = ['name', 'provence_abbr']


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'first_name', 'last_name', 'email', 'street', 'city', 'state']


class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['company_name', 'description', 'title', 'address_one', 'address_two', 'state']


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ['user', 'job', 'created_on', 'cover_letter', 'cover_letter_attachment', 'resume',
                    'resume_attachment']


admin.site.register(Provence, ProvenceAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
