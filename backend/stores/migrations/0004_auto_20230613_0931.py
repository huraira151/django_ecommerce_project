# Generated by Django 2.2.3 on 2023-06-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
