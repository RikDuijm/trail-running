# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-26 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200526_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
