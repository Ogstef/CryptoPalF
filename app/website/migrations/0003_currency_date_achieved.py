# Generated by Django 4.0.3 on 2022-04-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_currency_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='date_achieved',
            field=models.DateField(null=True),
        ),
    ]