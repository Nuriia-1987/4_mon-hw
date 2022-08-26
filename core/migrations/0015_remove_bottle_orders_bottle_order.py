# Generated by Django 4.1 on 2022-08-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_order_client'),
        ('core', '0014_bottlecount_description_bottlecount_expired'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottle',
            name='Orders',
        ),
        migrations.AddField(
            model_name='bottle',
            name='Order',
            field=models.ManyToManyField(blank=True, null=True, related_name='bottles', to='client.order', verbose_name='Заказы'),
        ),
    ]