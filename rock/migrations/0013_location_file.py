# Generated by Django 3.0.3 on 2020-08-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0012_remove_location_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
