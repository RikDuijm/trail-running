# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-12 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200312_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about_me',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
