# Generated by Django 4.2.6 on 2023-10-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_product_pimage_alter_product_pdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimage',
            field=models.ImageField(upload_to='appimage/product', verbose_name='Product Image'),
        ),
    ]
