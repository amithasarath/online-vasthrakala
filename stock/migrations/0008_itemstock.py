# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-24 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20180124_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_image', models.FileField(blank=True, null=True, upload_to=b'')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('description', models.TextField(blank=True, help_text='optional', max_length=200, null=True)),
                ('all_time_available', models.BooleanField(default=0)),
                ('item_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.ItemGroup')),
            ],
        ),
    ]
