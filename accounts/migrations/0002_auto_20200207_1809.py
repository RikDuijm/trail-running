# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-07 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, unique=True, upload_to='profile_images'),
        ),
    ]
