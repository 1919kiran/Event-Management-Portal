# Generated by Django 2.0.3 on 2018-04-11 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20180411_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 11, 19, 28, 48, 389943)),
        ),
        migrations.AlterField(
            model_name='event',
            name='tag',
            field=models.SlugField(max_length=16),
        ),
    ]
