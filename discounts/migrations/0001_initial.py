# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-28 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=254)),
                ('description_introduction', models.TextField(null=True)),
                ('description_first', models.TextField(null=True)),
                ('description_second', models.TextField(null=True)),
                ('description_third', models.TextField(blank=True, null=True)),
                ('normal_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('valid_until', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('views', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
            ],
        ),
    ]
