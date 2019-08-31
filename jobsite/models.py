from django.db import models
from django.contrib.auth.models import User as UserModel


class Provence(models.Model):
    name = models.CharField(max_length=50)
    provence_abbr = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class User(UserModel):
    street = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    state = models.ForeignKey(Provence, on_delete=models.SET_NULL, null=True)

    # returns first + last name if the user has provided them.
    # Otherwise returns required username
    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.username


class Job(models.Model):
    # Google cloud project ID
    project_id = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    # Job requisition ID.  Unique per job.
    requisition_id = models.CharField(max_length=50)
    description = models.TextField()
    job_application_url = models.TextField(default='https://www.example.org/job-posting/123')
    title = models.CharField(max_length=50)
    address_one = models.CharField(max_length=120)
    address_two = models.CharField(max_length=120)
    language_code = 'en-US'
    state = models.ForeignKey(Provence, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField()
    cover_letter_attachment = models.FileField(upload_to='documents/cover_letters/')
    resume = models.TextField()
    resume_attachment = models.FileField(upload_to='documents/resumes/')
