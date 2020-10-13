from django.db import models
from django.contrib.auth.models import User

class UserM(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def _str_(self):
        return self.username

class Profile(models.Model):
    profile_fname = models.CharField(max_length=50)
    profile_lname = models.CharField(max_length=50)
    profile_bio = models.CharField(max_length=500)
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        name = self.profile_fname + " " + profile_lname
        return name
