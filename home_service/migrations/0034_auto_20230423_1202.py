# Generated by Django 3.1.3 on 2023-04-23 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0033_auto_20230423_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='brandd',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='modell',
            new_name='model',
        ),
    ]
