# Generated by Django 2.1.15 on 2020-07-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200725_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='core/static/assets/img/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='core/static/video/'),
        ),
    ]