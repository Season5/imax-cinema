# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-15 21:25
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_schedule', '0014_auto_20160515_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 15, 21, 25, 37, 610661, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
