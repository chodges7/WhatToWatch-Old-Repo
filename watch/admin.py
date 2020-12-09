from django.contrib import admin
from . import models
from .models import Message

admin.site.register(Message)
admin.site.register(models.Profile)
admin.site.register(models.UserM)
