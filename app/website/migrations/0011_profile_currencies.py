# Generated by Django 4.0.3 on 2022-04-11 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_delete_registration_profile_email_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='currencies',
            field=models.ManyToManyField(to='website.currency'),
        ),
    ]
