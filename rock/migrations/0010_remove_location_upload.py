# Generated by Django 3.0.3 on 2020-08-24 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0009_location_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='upload',
        ),
    ]
