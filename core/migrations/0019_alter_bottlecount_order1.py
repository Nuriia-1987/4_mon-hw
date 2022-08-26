# Generated by Django 4.1 on 2022-08-26 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_order_client'),
        ('core', '0018_rename_order_bottlecount_order1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottlecount',
            name='order1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='client.order'),
        ),
    ]