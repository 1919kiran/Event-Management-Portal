# Generated by Django 2.0.3 on 2018-04-03 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20180403_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 3, 18, 27, 54, 215079)),
        ),
    ]
