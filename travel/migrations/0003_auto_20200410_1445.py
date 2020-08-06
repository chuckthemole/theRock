# Generated by Django 3.0.3 on 2020-04-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20200410_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='destination',
            name='zip_code',
            field=models.TextField(default=-1, max_length=10),
            preserve_default=False,
        ),
    ]
