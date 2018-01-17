# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from . models import ItemGroup


class ItemGroupListView(generic.ListView):
    template_name = 'stock/index.html'

    def get_queryset(self):
        return ItemGroup.objects.all()