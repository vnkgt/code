# Generated by Django 3.0.7 on 2020-07-11 13:39

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('djg04app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='chinainfo',
            managers=[
                ('CM', django.db.models.manager.Manager()),
            ],
        ),
    ]
