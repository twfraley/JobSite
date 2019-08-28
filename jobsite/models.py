from django.db import models


class Provence(models.Model):
    name = models.CharField(max_length=50)
    provence_abbr = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class User(models.User):
    street = models.TextField(max_length=50)
    city = models.TextField(max_length=50)
    state = models.ForeignKey(Provence, on_delete=models.CASCADE)

    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + self.last_name
        else:
            return self.username


class Job(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(Provence, on_delete=models.CASCADE)
    requirements = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    cover_letter = models.TextField()
    cover_letter_attachment = models.FileField(upload_to='documents/cover_letters/')
    cover_letter_uploaded_on = models.DateTimeField(auto_now_add=True)
    resume = models.TextField()
    resume_attachment = models.FileField(upload_to='documents/resumes/')
    resume_uploaded_on = models.DateTimeField(auto_now_add=True)
