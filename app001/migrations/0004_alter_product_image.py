# Generated by Django 4.0.3 on 2022-05-11 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0003_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
