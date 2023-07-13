# Generated by Django 4.0.4 on 2023-06-23 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0032_couponcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('postcode', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('amount', models.CharField(max_length=100)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
        ),
    ]
