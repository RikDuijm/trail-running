# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-12 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactuser',
            old_name='subject',
            new_name='title',
        ),
    ]
