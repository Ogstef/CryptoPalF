# Generated by Django 4.0.3 on 2022-04-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_currency_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='currency',
            name='avatar',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
