# Generated by Django 5.1.6 on 2025-02-11 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
