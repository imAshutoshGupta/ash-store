# Generated by Django 4.2.5 on 2023-10-23 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0004_product_pdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=0, upload_to='appimage/product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='pdetails',
            field=models.CharField(max_length=100, verbose_name='Product Description'),
        ),
    ]
