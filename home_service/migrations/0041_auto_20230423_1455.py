# Generated by Django 3.1.3 on 2023-04-23 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0040_remove_product_brand_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectmodel',
            name='selectbrand',
        ),
        migrations.DeleteModel(
            name='Selectbrand',
        ),
        migrations.DeleteModel(
            name='Selectmodel',
        ),
    ]
