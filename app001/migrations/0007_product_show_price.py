# Generated by Django 4.0.3 on 2022-05-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0006_alter_product_earnings_alter_product_value_to_yoli'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='show_price',
            field=models.BooleanField(default=True),
        ),
    ]
