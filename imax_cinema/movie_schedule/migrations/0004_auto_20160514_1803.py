# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-14 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_schedule', '0003_auto_20160513_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='pricing',
        ),
        migrations.AddField(
            model_name='ticket',
            name='pricing',
            field=models.ManyToManyField(to='movie_schedule.MoviePricing'),
        ),
    ]
