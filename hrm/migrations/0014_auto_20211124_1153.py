# Generated by Django 3.2.4 on 2021-11-24 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0013_auto_20211123_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='genlink',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 11, 53, 43, 251667), null=True),
        ),
    ]