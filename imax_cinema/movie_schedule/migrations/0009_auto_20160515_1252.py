# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-15 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_schedule', '0008_auto_20160515_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemaseat',
            name='seat',
            field=models.CharField(max_length=3),
        ),
    ]
