"""
Definition of models.
"""
#appname/models.py

from pickle import FALSE
from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Nonprofit(models.Model):
    # Define fields for the Donor model
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(unique=False, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    donation_link = models.CharField(max_length=100, blank=True, null=True)
    volunteer_link = models.CharField(max_length=100, blank=True, null=True)
    newspaper_signup = models.CharField(max_length=100, blank=True, null=True)
    rank = models.IntegerField(default=999, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # String representation of the Donor model

    def __str__(self):
        return f"{self.name}"

class Event(models.Model):
    # Define fields for the Donor model
    name = models.CharField(max_length=100)
    nonprofit_name = models.CharField(max_length=100)
    starts = models.CharField(max_length = 100, blank=False, null=True)
    ends = models.CharField(max_length = 100, blank=False, null=True)
    type = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    host_website = models.CharField(max_length=200, blank=True, null=True)
    rank = models.IntegerField(default=999, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # String representation of the Donor model

    def __str__(self):
        return f"{self.name}"
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def str(self):
        return self.user.username

class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=1000,blank=True)
    def __str__(self):
        return f"{self.name}"



