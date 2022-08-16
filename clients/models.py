from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.TextField(null=True, blank=True)
    bottles_ordered = models.IntegerField(default=10)
