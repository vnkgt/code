# Generated by Django 3.0.7 on 2020-07-11 13:49

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('djg04app', '0003_auto_20200711_2144'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='chinainfo',
            managers=[
                ('obj', django.db.models.manager.Manager()),
            ],
        ),
    ]
