# Generated by Django 4.1 on 2022-08-25 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_client_user'),
        ('core', '0006_remove_order_client_delete_client_delete_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottle',
            name='address',
        ),
        migrations.AddField(
            model_name='bottle',
            name='Order',
            field=models.ManyToManyField(blank=True, null=True, related_name='bottles', to='client.order', verbose_name='Заказы'),
        ),
    ]
