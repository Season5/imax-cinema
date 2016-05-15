# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-15 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_schedule', '0006_ticket_total_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='pricing',
        ),
        migrations.AddField(
            model_name='ticket',
            name='pricing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_schedule.MoviePricing'),
        ),
    ]