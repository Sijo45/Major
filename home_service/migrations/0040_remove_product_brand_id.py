# Generated by Django 3.1.3 on 2023-04-23 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0039_product_selectbrand_selectmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand_id',
        ),
    ]
