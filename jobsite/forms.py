from django import forms

from jobsite.models import Application, Job, User


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company_name', 'address_one', 'state']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['user_firstname', 'user_lastname', 'user_email', 'user_city', 'user_state', 'cover_letter', 'resume',
                  'resume_attachment']
        labels = {
            'user_state': 'State',
            'cover_letter': "Cover Letter: (Optional) Type or paste your cover letter here.",
            'resume': "Resume: Type your resume here or upload one below."
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'street', 'city', 'state']


class SearchForm(forms.Form):
    pass
