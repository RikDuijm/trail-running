# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-29 17:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200229_1711'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventSeptember',
            new_name='Event',
        ),
        migrations.DeleteModel(
            name='EventOctober',
        ),
        migrations.DeleteModel(
            name='Months',
        ),
    ]
