# Generated by Django 4.0.4 on 2023-05-15 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_upcomingproductimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingproductimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.upcomingproduct'),
        ),
    ]
