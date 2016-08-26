# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='month',
            field=models.CharField(default=b'NO DATA', editable=False, max_length=10),
        ),
        migrations.AddField(
            model_name='weather',
            name='year',
            field=models.IntegerField(default=b'0000', editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='weather',
            name='value',
            field=models.FloatField(max_length=10),
        ),
    ]