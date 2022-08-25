from django.db import models


# Create your models here.

class Bottle(models.Model):
    volume = models.ImageField(default=10)
    address = models.CharField(max_length=255)
    maker = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    expired = models.BooleanField(default=True)


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=True, verbose_name="Является активным покупателем")
    bottles_ordered = models.IntegerField(default=10)
    photo = models.ImageField(
        verbose_name="Фото",
        upload_to='photos',
        null=True,
        blank=True
    )


class Order(models.Model):
    client = models.ForeignKey(
        to=Client, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="orders"
    )
    created_at = models.DateTimeField(
        verbose_name="Дата и время создания заказа",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата и время изменения заказа",
        auto_now=True,
    )
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    finished = models.BooleanField(default=False)

    def __init__(self):
        return f"{self.name} - {self.contacts}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
