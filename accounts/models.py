# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.

class ClientType(models.Model):
    client_type = models.CharField(max_length=50)

    def __str__(self):
        return self.client_type


class Reseller(models.Model):
    reseller_name = models.CharField(max_length=100)

    def __str__(self):
        return self.reseller_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name


class Dealer(models.Model):
    dealer_name =models.CharField(max_length=100)
    dealer_code =models.CharField(max_length=5,primary_key=True)

    def __str__(self):
        return self.dealer_code


class SalesOrder(models.Model):
    client_type     = models.ForeignKey(ClientType,on_delete=models.CASCADE)
    reseller        = models.ForeignKey(Reseller,on_delete=models.CASCADE)
    new_reseller    = models.BooleanField(default=False)
    customer        = models.ForeignKey(Customer,on_delete=models.CASCADE)
    new_customer    = models.BooleanField(default=False)
    type            = models.ForeignKey('stock.ItemType',on_delete=models.CASCADE)
    cost_price      =   models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    selling_price   =   models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    profit          =   models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    dealer_code    = models.ForeignKey(Dealer,on_delete=models.CASCADE)
    booking_date    =  models.DateField(default=datetime.date.today)
    tracking_id     = models.CharField(max_length=100)
    qty            = models.IntegerField(default=False)

    def __int__(self):
        return self.id
    