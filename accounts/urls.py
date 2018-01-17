from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$',views.showDashboard,name='dashboard'),
    url(r'^dealers/$',views.show_dealers,name='dealers'),
    url(r'^resellers/$',views.show_resellers,name='resellers'),
    url(r'^customers/$',views.show_customers,name='customers'),

    url(r'^delete-dealers/$',views.delete_dealer,name='delete_dealer'),
    url(r'^delete-resellers/$',views.delete_reseller,name='delete_reseller'),
    url(r'^delete-customers/$',views.delete_customer,name='delete_customer'),

    url(r'^order/$',views.make_so,name = 'make_so'),
    url(r'^orders/$',views.SOListView.as_view(),name = 'so_list'),

]