# Generated by Django 3.2.5 on 2021-12-18 16:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0010_auto_20211218_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='name',
        ),
        migrations.AddField(
            model_name='history',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='calc.record'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 17, 6, 6, 434)),
        ),
    ]