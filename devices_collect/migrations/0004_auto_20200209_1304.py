# Generated by Django 3.0.3 on 2020-02-09 05:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('devices_collect', '0003_auto_20200209_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectdevices',
            name='generated_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 9, 5, 4, 22, 379333, tzinfo=utc)),
        ),
    ]
