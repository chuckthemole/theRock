# Generated by Django 3.0.3 on 2020-08-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0004_auto_20200813_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='sport_location_img',
            field=models.ImageField(blank=True, default='static/rock/images/no_image_available.PNG', upload_to='images/'),
        ),
    ]