# Generated by Django 4.0.3 on 2022-04-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_currency_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
