from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    aboutMe = models.TextField(max_length=2000)
    address = models.TextField(max_length=200)
    github_link = models.URLField(
        max_length=128,
        db_index=True,
        blank=True
    )
    linkedIn_link = models.URLField(
        max_length=128,
        db_index=True,
        blank=True
    )
    college = models.CharField(max_length=200)
    degree_college = models.CharField(max_length=200)
    cgpa_college = models.CharField(max_length=200)
    time_college = models.CharField(max_length=200)

    class12 = models.CharField(max_length=200)
    score_12th = models.CharField(max_length=200)
    stream_12th = models.CharField(max_length=200)
    time_class12 = models.CharField(max_length=200)

    prev_work_company = models.CharField(max_length=200)
    prev_work_role = models.CharField(max_length=200)
    prev_work_location = models.CharField(max_length=200)
    prev_work_description = models.TextField(max_length=2000)

    proj_title = models.CharField(max_length=200)
    proj_description = models.TextField(max_length=2000)

    languages = models.TextField(max_length=200)
    tools_and_framework = models.TextField(max_length=200)
