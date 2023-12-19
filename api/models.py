from django.db import models

# Create your models here.
class Member(models.Model):
    email = models.CharField(max_length=50, primary_key = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    git_url = models.CharField(max_length=100, blank = True, null = True)
    linkedIn_url= models.CharField(max_length=100, blank = True, null = True)
    comment = models.CharField(max_length=200)
