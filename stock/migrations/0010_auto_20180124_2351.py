# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-24 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_auto_20180124_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemstock',
            name='item_image',
            field=models.FileField(blank=True, null=True, upload_to='stock/media/items/'),
        ),
    ]
