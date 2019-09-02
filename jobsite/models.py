from django.db import models
from django.contrib.auth.models import User as UserModel


class Province(models.Model):
    name = models.CharField(max_length=50)
    province_abbr = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class User(UserModel):
    """
    Standard built-in User model.
    Required fields: username, password
    useful optional fields: first_name, last_name, email
    Documentation: https://docs.djangoproject.com/en/2.2/ref/contrib/auth/#user-model
    """

    street = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    state = models.ForeignKey(Province, on_delete=models.PROTECT)

    # Returns first + last name if the user has provided them. Otherwise returns required username
    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.username


class Job(models.Model):
    """
    TODO: integrate with Google Cloud Talent API
    Job object (mirrors required fields on Google Cloud Talent API)
    Google Cloud Talent API Quickstart:
    https://cloud.google.com/talent-solution/job-search/docs/quickstart-jobs-and-companies
    Google Cloud Talent API Documentation:
    https://cloud.google.com/talent-solution/job-search/docs/reference/rest/
    """

    # Google cloud project ID.  Required for Google Talent API
    # project_id = models.CharField(max_length=50)  # Get from talent_api_service.py

    # Job requisition ID.  Unique per job. Required for Google Talent API
    # requisition_id = models.CharField(max_length=50) # Get from talent_api_service.py(?)

    # URL of original posting on site.  Handy for Google Talent API
    # job_application_url = models.TextField(default='https://www.example.org/job-posting/123')

    # Localization.  Required for Google Talent API
    # language_code = 'en-US'

    company_name = models.CharField(max_length=50)
    description = models.TextField()
    title = models.CharField(max_length=50)
    address_one = models.CharField(max_length=120)
    address_two = models.CharField(max_length=120)
    state = models.ForeignKey(Province, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Application(models.Model):
    """
    Foreign Key linking Job.
    Includes both text field and file uploads for cover letter and resume (for now?)
    """
    # User Foreign Key relationship - not needed for simple application
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    user_firstname = models.CharField(max_length=30)
    user_lastname = models.CharField(max_length=30)
    user_email = models.EmailField()
    user_city = models.CharField(max_length=50)
    user_state = models.ForeignKey(Province, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField(blank=True)
    cover_letter_attachment = models.FileField(upload_to='documents/cover_letters/', blank=True)
    resume = models.TextField(blank=True)
    resume_attachment = models.FileField(upload_to='documents/resumes/', blank=True)
