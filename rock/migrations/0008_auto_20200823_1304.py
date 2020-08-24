# Generated by Django 3.0.3 on 2020-08-23 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0007_auto_20200815_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='sport_location_img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rock.Upload'),
        ),
    ]
