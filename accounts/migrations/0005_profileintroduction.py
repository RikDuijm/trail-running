# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-03 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileIntroduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField(blank=True, null=True)),
            ],
        ),
    ]