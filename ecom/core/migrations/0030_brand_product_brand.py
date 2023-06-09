# Generated by Django 4.0.4 on 2023-05-25 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_color_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.brand'),
        ),
    ]
