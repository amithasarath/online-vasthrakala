# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ItemType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class ItemGroup(models.Model):
    group = models.CharField(max_length=50)
    group_image = models.FileField()
    price = models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    type = models.ForeignKey(ItemType,on_delete=models.CASCADE)
    description = models.TextField(max_length=200,blank=True,help_text="optional")
    all_time_available =models.BooleanField(default=0)

    def __str__(self):
        return self.group