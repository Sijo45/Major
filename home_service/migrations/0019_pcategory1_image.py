# Generated by Django 3.1.3 on 2023-03-26 22:52

from django.db import migrations, models
import home_service.models


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0018_auto_20230326_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcategory1',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path),
        ),
    ]