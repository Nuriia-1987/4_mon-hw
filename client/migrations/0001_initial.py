# Generated by Django 4.1 on 2022-08-26 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True, verbose_name='Является активным покупателем')),
                ('bottles_ordered', models.IntegerField(default=1)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фото')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания заказа')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения заказа')),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('contacts', models.CharField(max_length=255)),
                ('finished', models.BooleanField(default=False)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='client.client')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
