from django.conf.urls import url, include
from .views import products_list, product_detail


urlpatterns = [
    url(r'^$', products_list, name='products_list'),
    url(r'^(?P<product_id>\d+)/$', product_detail, name='product_detail'),
    url(r'^(?P<category_name>[-\w]+)/$', products_list, name='products_list'),
]