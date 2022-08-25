from django.db import models


class Bottle(models.Model):
    volume = models.IntegerField(default=10)
    address = models.CharField(max_length=255)
    maker = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    expired = models.BooleanField(default=True)


