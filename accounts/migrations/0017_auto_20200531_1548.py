# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-31 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_remove_userprofile_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepost',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
