# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-04 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20200303_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='normal_price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='valid_until',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
