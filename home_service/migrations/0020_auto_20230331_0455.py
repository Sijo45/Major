# Generated by Django 3.1.3 on 2023-03-30 23:25

from django.db import migrations, models
import home_service.models


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0019_pcategory1_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path),
        ),
    ]
