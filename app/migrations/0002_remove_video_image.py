# Generated by Django 2.1.15 on 2020-07-25 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='image',
        ),
    ]
