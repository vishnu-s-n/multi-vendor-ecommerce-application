# Generated by Django 4.0.4 on 2023-05-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/slider_images')),
                ('discount_deal', models.CharField(choices=[('HOT-DEALS', 'HOTDEALS'), ('NEW-ARRIVALS', 'NEW-ARRIVALS')], max_length=100)),
                ('sale', models.IntegerField()),
                ('brand_name', models.CharField(max_length=200)),
                ('discount', models.IntegerField()),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
