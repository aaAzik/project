# Generated by Django 4.2.6 on 2023-11-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoop', '0003_alter_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]