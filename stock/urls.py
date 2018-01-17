from django.conf.urls import url
from . views import ItemGroupListView

from django.conf import settings
from django.conf.urls.static import static

app_name='stock'

urlpatterns = [
    url(r'^$',ItemGroupListView.as_view(),name="index"),
]