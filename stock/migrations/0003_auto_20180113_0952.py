# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_itemgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemgroup',
            old_name='group_type',
            new_name='type',
        ),
    ]
