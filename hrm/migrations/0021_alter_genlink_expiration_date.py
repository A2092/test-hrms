# Generated by Django 5.0.1 on 2024-01-13 21:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0020_alter_genlink_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genlink',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 21, 59, 40, 791581), null=True),
        ),
    ]
