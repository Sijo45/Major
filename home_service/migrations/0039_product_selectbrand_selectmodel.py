# Generated by Django 3.1.3 on 2023-04-23 09:06

from django.db import migrations, models
import django.db.models.deletion
import home_service.models


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0038_auto_20230423_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selectbrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Selectmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('selectbrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_service.selectbrand')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('brand_id', models.IntegerField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path)),
                ('product_image1', models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path)),
                ('product_image2', models.ImageField(blank=True, null=True, upload_to=home_service.models.get_file_path)),
                ('small_description', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_service.pcategory1')),
            ],
        ),
    ]