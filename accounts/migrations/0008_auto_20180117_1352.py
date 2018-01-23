# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 13:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_salesorder_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorder',
            name='client_type',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='dealer_code',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='reseller',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='type',
        ),
        migrations.DeleteModel(
            name='SalesOrder',
        ),
    ]