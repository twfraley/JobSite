from django import forms

from jobsite.models import Application, Job, User


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company_name', 'description', 'title', 'address_one', 'address_two', 'state']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'cover_letter_attachment', 'resume', 'resume_attachment']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'street', 'city', 'state']
