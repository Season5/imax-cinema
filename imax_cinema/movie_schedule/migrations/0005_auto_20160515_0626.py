# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-15 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_schedule', '0004_auto_20160514_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='number_of_tickets',
        ),
        migrations.AddField(
            model_name='ticket',
            name='number_of_regular_tickets',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='number_of_student_tickets',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='height_field',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='width_field',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='moviepricing',
            name='regular_fee',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='moviepricing',
            name='student_fee',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
