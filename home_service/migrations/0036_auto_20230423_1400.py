# Generated by Django 3.1.3 on 2023-04-23 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0035_auto_20230423_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model_name',
        ),
    ]
