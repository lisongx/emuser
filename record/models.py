from django.db import models


class Record(models.Model):

    source = models.CharField(max_length=32)
    subject = models.CharField(max_length=128)
    url = models.URLField(max_length=128)
    picture_url = models.URLField(max_length=128, null=True)
    datetime = models.DateTimeField()
