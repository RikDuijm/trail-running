# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-04 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='age',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='gender',
            field=models.CharField(choices=[('optional', 'Fill out when you participate in a race'), ('male', 'male'), ('female', 'female')], default='optional', max_length=10),
        ),
    ]