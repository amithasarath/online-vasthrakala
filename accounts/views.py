# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . models import Dealer,Reseller,Customer,SalesOrder
from . forms import DealerForm,ResellerForm,CustomerForm,SalesOrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views import generic
from django.contrib import messages
from django.db.models import Max,Sum,Min,Count,Avg

def showDashboard(request):
    return render(request,'accounts/dashboard.html')


def show_dealers(request):
    all_dealers = Dealer.objects.all()
    if request.method == "POST":
        form = DealerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("accounts:dealers"))
    else:
        form = DealerForm()

    return  render(request,'accounts/dealer.html',{'form':form,'dealers':all_dealers})


def show_resellers(request):
    # all_resellers = Reseller.objects.all()
    all_resellers = Reseller.objects.order_by('id').reverse()
    if request.method == "POST":
        form = ResellerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("accounts:resellers"))
    else:
        form = ResellerForm()

    return  render(request,'accounts/reseller.html',{'form':form,'resellers':all_resellers})


def show_customers(request):
    # all_customers = Customer.objects.filter().order_by('id')
    all_customers = Customer.objects.order_by('id').reverse()
    if request.method == "POST":
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("accounts:customers"))
    else:
        form = CustomerForm()

    return  render(request,'accounts/customer.html',{'form':form,'customers':all_customers})


def make_so(request):
    all_orders = SalesOrder.objects.all()
    if request.method == "POST":
        form = SalesOrderForm(request.POST)
        # print form
        if form.is_valid():
            form.save()
            # messages.info(request, 'Your order has been saved successfully!')
            return HttpResponseRedirect(reverse("accounts:make_so"))
    else:
        form = SalesOrderForm()

    return render(request,'accounts/order.html',{'form':form,"orders":all_orders})


class SOListView(generic.ListView):
    model = SalesOrder
    # OR
    # queryset = SalesOrder.objects.all()
    template_name = "accounts/order_list.html"
    context_object_name = "all_orders"
    profit = SalesOrder.objects.all().aggregate(Sum('selling_price'))
    # print profit
    # print "#" * 50

    def get_context_data(self, **kwargs):
        context = super(SOListView, self).get_context_data(**kwargs)
        context['profit'] = SalesOrder.objects.all().aggregate(Sum('selling_price'))
                            # - SalesOrder.objects.all().aggregate(Sum('cost_price'))
        context['sp'] = SalesOrder.objects.all().aggregate(Sum('selling_price'))
        print context['profit']['selling_price__sum']
        return context


def delete_dealer(request):
    if request.method == "POST":
        dealer_id = request.POST.get("dealer_id")
        dealer = Dealer.objects.get(dealer_code = dealer_id)
        dealer.delete()
        return HttpResponseRedirect(reverse("accounts:dealers"))
    else:
        return HttpResponseRedirect(reverse("accounts:dealers"))


def delete_reseller(request):
    if request.method == "POST":
        reseller_id = request.POST.get("reseller_id")
        reseller = Reseller.objects.get(id = reseller_id)
        reseller.delete()
        return HttpResponseRedirect(reverse("accounts:resellers"))
    else:
        return HttpResponseRedirect(reverse("accounts:resellers"))


def delete_customer(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
        customer = Customer.objects.get(id = customer_id)
        customer.delete()
        return HttpResponseRedirect(reverse("accounts:customers"))
    else:
        return HttpResponseRedirect(reverse("accounts:customers"))

