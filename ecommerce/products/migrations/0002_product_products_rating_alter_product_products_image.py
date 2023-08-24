# Generated by Django 4.2.4 on 2023-08-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='products_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='products_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]