# Generated by Django 3.0.3 on 2020-08-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0006_auto_20200814_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rocker',
            name='local',
        ),
        migrations.RemoveField(
            model_name='rocker',
            name='rocker_yet',
        ),
        migrations.AlterField(
            model_name='location',
            name='sport_location_img',
            field=models.ImageField(blank=True, default='static/rock/images/no_image_available.PNG', upload_to='images/'),
        ),
    ]
