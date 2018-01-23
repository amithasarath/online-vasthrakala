# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from . models import Dealer,Reseller,Customer,SalesOrder
from . forms import DealerForm,ResellerForm,CustomerForm,SalesOrderForm
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy

from django.views import generic
from django.contrib import messages
from django.db.models import Max,Sum,Min,Count,Avg,Q

from django.utils import timezone

import xlwt
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  SalesOrderSerializer

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
        if form.is_valid():
            so = form.save(commit=False)
            so.created = timezone.now()
            so.save()
            # messages.info(request, 'Your order has been saved successfully!')
            return HttpResponseRedirect(reverse("accounts:make_so"))
    else:
        form = SalesOrderForm()

    return render(request,'accounts/salesorder_form.html',{'form':form,"orders":all_orders})


def update_so(request,pk):
    # all_orders = SalesOrder.objects.all()
    # print pk
    so = get_object_or_404(SalesOrder, id=pk)
    # print so
    if request.method == "POST":
        form = SalesOrderForm(request.POST,instance=so)
        print form
        # print form.id
        print (form.errors)
        if form.is_valid():
            so = form.save(commit=False)
            so.modified = timezone.now()
            so.save()
            # messages.info(request, 'Your order has been saved successfully!')
            # return redirect("accounts:update_so",pk=so.id)
            # return redirect("accounts:so_detail",pk=so.id)
            return redirect("accounts:so_list")
            # return HttpResponseRedirect(reverse("accounts:so_detail",id=so.id))
    else:
        form = SalesOrderForm(instance =so)
        print "FORM GET"
        print form

    return render(request,'accounts/salesorder_update_form.html',{'form':form})
    # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class SalesOrderUpdateView(generic.UpdateView):
    model = SalesOrder
    fields = "__all__"
    template_name_suffix = '_update_form'
    # template_name = "accounts/salesorder_update.html"

class SalesOrderDeleteView(generic.DeleteView):
    model = SalesOrder
    fields = "__all__"
    # template_name_suffix = '_update_form'
    success_url = reverse_lazy('accounts:so_list')


class SalesOrderDetailView(generic.DetailView):
    model = SalesOrder
    template_name_suffix = '_detail'
    template_name = "accounts/salesorder_detail.html"

    def get_context_data(self, **kwargs):
        context = super(SalesOrderDetailView,self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


class SOListView(generic.ListView):
    model = SalesOrder
    # OR
    # queryset = SalesOrder.objects.all()
    template_name = "accounts/order_list.html"
    context_object_name = "all_orders"
    profit = SalesOrder.objects.all().aggregate(Sum('selling_price'))

    def get_context_data(self, **kwargs):
        context = super(SOListView, self).get_context_data(**kwargs)
        context['profit'] = SalesOrder.objects.all().aggregate(Sum('selling_price'))
                            # - SalesOrder.objects.all().aggregate(Sum('cost_price'))
        context['sp'] = SalesOrder.objects.all().aggregate(Sum('selling_price'))
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


class SalesOrderSearchView(generic.ListView): #Not using now
    template_name = 'accounts/report-sales.html'
    model = SalesOrder

    def get_queryset(self):
        try:
            dealer = self.request.GET.get('dealer_code')
            customer = self.request.GET.get('customer')
            # dealer = self.kwargs.get('dealer_code',"kys")
            print "*" * 100
            print dealer
            print customer
            print "Here"
        except:
            dealer = ''
        if (dealer != ''):
            object_list = self.model.objects.filter(dealer_code = dealer)
        else:
            object_list = self.model.objects.all()
        print "Dealer", dealer
        print "+" *100
        print object_list
        return object_list


def custom_sales_report(request):
    if request.method == "POST":
        pass
    else:
        print "-" * 100

        r = request.GET.get('reseller') or ""
        c = request.GET.get('customer') or ""
        d = request.GET.get('dealer_code') or ""
        cp = request.GET.get('cp') or ""
        sp = request.GET.get('sp') or ""
        bd = request.GET.get('booking_date') or ""
        ty = request.GET.get('type') or ""
        s = request.GET.get('order_status') or ""
        tr = request.GET.get('tracking_id') or ""

        resellers = Reseller.objects.all()
        customers = Customer.objects.all()
        dealers = Dealer.objects.all()
        so = sos = SalesOrder.objects.all()
        print sos

        # if r:
        print "YES"
        # so = sos.filter(booking_date__year=2017)
        # so = sos.filter(tracking_id__startswith='123')
        # so = sos.filter(tracking_id__contains='456')
        so = sos.filter(reseller__reseller_name__contains=r)
        print so

        # so = SalesOrder.objects.get(
        # so = sos.filter(
        #     Q(reseller__reseller_name__contains=r) |
        #     Q(customer__customer_name__contains=c) |
        #     Q(dealer_code=d) |
        #     Q(tracking_id__startswith = tr) ,
        #     # tracking_id__startswith= tr
        #     order_status = s
        # )

        query =Q()

        if r:
            query = Q(reseller__reseller_name__contains=r)

        if c:
            query = query & Q(customer__customer_name__contains=c)

        if d:
            query = query & Q(dealer_code = d)

        if cp:
            query = query & Q(cost_price = cp)

        if sp:
            query = query & Q(selling_price = sp)

        if bd:
            query = query & Q(booking_date = bd)

        if ty:
            query = query & Q(type = ty)

        if s:
            query = query & Q(order_status = s)

        if tr:
            query = query & Q(tracking_id = tr)

        # query = query1 | query2

        result_so = SalesOrder.objects.filter(query)

        context = {
            "resellers_list":resellers,
            "customers_list":customers,
            "dealers_list":dealers,
            "so_list":result_so,
            "report":"custom",
        }

    return render(request,'accounts/report-sales.html',context)


def daily_sales_report(request):
    if request.method == "POST":
        pass
    else:
        bd = request.GET.get('booking_date') or ""

        resellers = Reseller.objects.all()
        customers = Customer.objects.all()
        dealers = Dealer.objects.all()
        # so = sos = SalesOrder.objects.all()
        # print so

        query =Q()

        if bd:
            query = Q(booking_date = bd)

        # query = query1 | query2

        result_so = SalesOrder.objects.filter(query)

        context = {
            "resellers_list": resellers,
            "customers_list": customers,
            "dealers_list": dealers,
            "so_list": result_so,
            "report": "daily"
        }

    return render(request,'accounts/report-sales.html',context)


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First name', 'Last name', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


class SalesOrderList(APIView):  #url : accounts/api/sales-order-list

    def get(self,request):
        sales_orders = SalesOrder.objects.all()
        so_serailizer = SalesOrderSerializer(sales_orders,many=True)
        print type(so_serailizer.data)
        return Response(so_serailizer.data)