# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import  ClientType, Reseller,Customer,Dealer,SalesOrder
# Register your models here.
admin.site.register(ClientType)
admin.site.register(Reseller)
admin.site.register(Customer)
admin.site.register(SalesOrder)
admin.site.register(Dealer)