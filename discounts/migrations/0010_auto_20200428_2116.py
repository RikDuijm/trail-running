# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-28 21:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0009_auto_20200427_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ClothesSize',
        ),
        migrations.DeleteModel(
            name='ShoeSize',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='sku',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discounts.Product'),
        ),
    ]
