# Generated by Django 2.0.3 on 2018-04-04 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_auto_20180404_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 4, 12, 20, 47, 577168)),
        ),
    ]
