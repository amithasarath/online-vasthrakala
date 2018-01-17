# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=50)),
                ('group_image', models.FileField(upload_to=b'')),
                ('group_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.ItemType')),
            ],
        ),
    ]
