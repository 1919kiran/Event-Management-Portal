# Generated by Django 2.0.3 on 2018-04-04 05:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_auto_20180404_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 4, 11, 0, 10, 959683)),
        ),
    ]
