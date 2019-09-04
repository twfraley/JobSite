from django.db import models
from django.contrib.auth.models import User as UserModel


class Province(models.Model):
    name = models.CharField(max_length=50)
    province_abbr = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


# Not used.  See green comment text below.
class User(UserModel):
    """
    Implemented too late for this project; Ideally would reference AbstractUser from the start.
    Changing User Auth schemes after making migrations or running the app is tricky.
    Info: https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#extending-user
    """

    street = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    state = models.ForeignKey(Province, on_delete=models.PROTECT)

    # Returns first + last name if the user has provided them. Otherwise returns required username
    def __str__(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
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

    company_name = models.CharField(max_length=50, default='JobSite!')
    description = models.TextField()
    title = models.CharField(max_length=50)
    address_one = models.CharField(max_length=120)
    address_two = models.CharField(max_length=120, blank=True)
    state = models.ForeignKey(Province, on_delete=models.PROTECT)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    """
    Foreign Key linking Job.
    Includes both text field and file uploads for cover letter and resume (for now?)
    """
    # User Foreign Key relationship - not needed for simple application
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    user_firstname = models.CharField("First Name", max_length=30)
    user_lastname = models.CharField("LastName", max_length=30)
    user_email = models.EmailField("Email")
    user_city = models.CharField("City", max_length=50)
    user_state = models.ForeignKey(Province, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField(blank=True)
    resume = models.TextField(blank=True)
    resume_attachment = models.FileField("Upload a Resume", upload_to='documents/resumes/%Y/%m/%d/', blank=True)


class UserApplication(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
