# Generated by Django 3.2.5 on 2021-12-18 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_alter_record_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='name',
        ),
        migrations.AddField(
            model_name='history',
            name='name',
            field=models.ManyToManyField(to='calc.Record'),
        ),
        migrations.AlterField(
            model_name='record',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 17, 4, 3, 707499)),
        ),
    ]
