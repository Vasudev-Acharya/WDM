# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_data', '0002_auto_20160825_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='value',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='weather',
            unique_together=set([('id', 'region', 'type'), ('region', 'month', 'year')]),
        ),
    ]
