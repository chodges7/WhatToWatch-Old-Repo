from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
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
    profile_image = models.ImageField(upload_to='watch/static/profile-pics',
        default='watch/static/LogoColor.png', null=True, blank=True)

    def __str__(self):
        name = self.profile_fname + " " + self.profile_lname
        return name
User = get_user_model()
class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]