# Generated by Django 4.1 on 2022-08-26 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_rename_orders_order'),
        ('core', '0011_alter_bottle_order_alter_bottlecount_bottle'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottlecount',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='client.order'),
        ),
    ]
