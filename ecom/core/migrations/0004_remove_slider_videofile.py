# Generated by Django 4.0.4 on 2023-05-10 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_slider_image_slider_videofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='videofile',
        ),
    ]
