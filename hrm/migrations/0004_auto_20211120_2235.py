# Generated by Django 3.2.4 on 2021-11-20 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0003_alter_genlink_expiration_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genlink',
            old_name='employee',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='genlink',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 22, 35, 49, 548177), null=True),
        ),
    ]