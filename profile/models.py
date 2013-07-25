from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    url = models.URLField(max_length=256, blank=True, null=True)
    bio = models.CharField(max_length=256, blank=True, null=True)
