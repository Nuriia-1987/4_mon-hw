# Generated by Django 4.1 on 2022-08-26 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_bottlecount'),
        ('client', '0003_alter_client_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
    ]