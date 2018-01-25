from django import forms
from . models import Dealer,Reseller,Customer,SalesOrder


class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = '__all__'

class ResellerForm(forms.ModelForm):
    class Meta:
        model = Reseller
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = '__all__'
        # fields = ['reseller','customer','dealer_code','cost_price','selling_price','order_status']