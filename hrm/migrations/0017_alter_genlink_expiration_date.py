# Generated by Django 3.2.4 on 2021-11-24 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0016_auto_20211124_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genlink',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 14, 26, 55, 926624), null=True),
        ),
    ]