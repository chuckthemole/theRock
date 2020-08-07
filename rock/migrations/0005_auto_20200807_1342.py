# Generated by Django 3.0.3 on 2020-08-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0004_auto_20200807_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.RemoveField(
            model_name='location',
            name='country',
        ),
        migrations.RemoveField(
            model_name='location',
            name='is_my_location',
        ),
        migrations.RemoveField(
            model_name='location',
            name='is_visiting',
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.TextField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='location',
            name='zip',
            field=models.TextField(default='', max_length=5),
        ),
    ]
