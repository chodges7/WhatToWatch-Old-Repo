from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Profile(models.Model):
    profile_fname = models.CharField(max_length=50)
    profile_lname = models.CharField(max_length=50)
    profile_bio = models.CharField(max_length=500)
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='watch/static/profile-pics',
        default='watch/static/LogoColor.png', null=True, blank=True)

    def __str__(self):
        name = self.profile_fname + " " + self.profile_lname
        return name
