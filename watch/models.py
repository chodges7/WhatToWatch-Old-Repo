from django.db import models
from django.contrib.auth.models import User

class UserM(models.Model):
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def _str_(self):
        return self.username