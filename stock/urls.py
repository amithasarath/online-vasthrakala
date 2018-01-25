from django.conf.urls import url
from . views import ItemGroupListView,item_stock_list,ItemStockDetailView,view_cart,checkout

from django.conf import settings
from django.conf.urls.static import static

app_name='stock'

urlpatterns = [
    url(r'^$',ItemGroupListView.as_view(),name="index"),
    # url(r'^products/$',ItemStockListView.as_view(),name="products"),
    url(r'^products/(?P<pk>[0-9]+)/$',item_stock_list,name="products"),
    url(r'^products/details/(?P<pk>[0-9]+)/$',
        ItemStockDetailView.as_view(),name="product-detail"),
    url(r'^cart/$',view_cart,name="cart"),
    url(r'^checkout/$',checkout,name="checkout"),
]