# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-12 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0002_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('watches', 'watches'), ('clothes', 'clothes'), ('shoes', 'shoes'), ('events', 'events')], default='shoes', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=2),
        ),
    ]
