# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from . models import ItemGroup,ItemStock


class ItemGroupListView(generic.ListView):
    template_name = 'stock/index.html'
    model = ItemGroup

    # def get_queryset(self):
    #     return ItemGroup.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ItemGroupListView,self).get_context_data(**kwargs)
        sarees = ItemGroup.objects.all().filter(type=2)
        churidars = ItemGroup.objects.all().filter(type=1)
        jewels = ItemGroup.objects.all().filter(type=3)

        context["saree_list"]       = sarees
        context["churidar_list"]    = churidars
        context["jewel_list"]       = jewels

        # context.update({
        #     'saree_list': sarees,
        #     'churidar_list': churidars,
        #     'jewel_list': jewels,
        # })
        print sarees
        return context


class ItemStockListView(generic.ListView):
    template_name = 'stock/products.html'

    def get_queryset(self):
        return ItemStock.objects.all()


def item_stock_list(request,pk):
    print pk
    print "-" *100
    if pk == "0":
        item_list = ItemStock.objects.all()
    else:
        item_list = ItemStock.objects.filter(item_group = pk)
    for item in item_list:
        print item.id
        print item.item_name
    return render(request,'stock/products.html',{"item_list":item_list})

class ItemStockDetailView(generic.DetailView):
    model = ItemStock
    template_name = 'stock/product_detail.html'


def view_cart(request):
    return render(request,'stock/cart.html')

def checkout(request):
    return render(request, 'stock/checkout.html')
