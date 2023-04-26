# Generated by Django 3.1.3 on 2023-04-23 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0031_auto_20230423_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_service.selectbrand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_service.selectmodel'),
        ),
    ]