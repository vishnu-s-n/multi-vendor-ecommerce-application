# Generated by Django 4.0.4 on 2023-05-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_slider_videofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='image',
            field=models.ImageField(null=True, upload_to='media/slider_images'),
        ),
    ]
