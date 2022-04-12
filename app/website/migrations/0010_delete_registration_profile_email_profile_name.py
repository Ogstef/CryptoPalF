# Generated by Django 4.0.3 on 2022-04-11 18:02

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default=1, max_length=100, verbose_name=django.contrib.auth.models.User),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=0, max_length=150, verbose_name=django.contrib.auth.models.User),
            preserve_default=False,
        ),
    ]