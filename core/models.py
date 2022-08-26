from django.db import models
from client.models import Order


class Bottle(models.Model):
    volume = models.IntegerField(default=10)
    maker = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    expired = models.BooleanField(default=True)

    orders = models.ManyToManyField(
        to=Order, null=True, blank=True,
        verbose_name='Orders',
        related_name='bottles'
    )


class BottleCount(models.Model):
    bottle = models.ForeignKey(
        to=Bottle, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="count",
    )
    count = models.IntegerField(default=1)

    order1 = models.ForeignKey(
        to=Order, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="order"
    )
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bottle} - {self.count}"
