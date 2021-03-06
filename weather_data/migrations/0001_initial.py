# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Region',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=10)),
                ('type', models.CharField(choices=[(b'Tmin', b'Tmin'), (b'TMax', b'TMax'), (b'TMean', b'TMean'), (b'Rainfall', b'Rainfall'), (b'Sunshine', b'Sunshine')], max_length=10)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_data.Region')),
            ],
            options={
                'db_table': 'Weather',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='region',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='weather',
            unique_together=set([('id', 'region', 'type')]),
        ),
    ]
