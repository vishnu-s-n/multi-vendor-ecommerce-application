# Generated by Django 4.0.4 on 2023-05-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_rename_image_url_upcomingproductimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingproductimages',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
