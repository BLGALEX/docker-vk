# Generated by Django 3.2.9 on 2021-11-04 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_api', '0003_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
    ]
