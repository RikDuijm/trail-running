# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-20 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200520_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='personal_messages'),
        ),
    ]
