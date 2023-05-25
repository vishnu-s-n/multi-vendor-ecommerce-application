# Generated by Django 4.0.4 on 2023-05-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_slider_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='image',
        ),
        migrations.AddField(
            model_name='slider',
            name='videofile',
            field=models.FileField(null=True, upload_to='media/slider_video', verbose_name='videos'),
        ),
    ]
