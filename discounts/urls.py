from django.conf.urls import url, include
from .views import products_list, product_detail
from cart.views import add_to_cart

urlpatterns = [
    url(r'^$', products_list, name='products_list'),
    url(r'^(?P<product_id>\d+)/$', product_detail, name='product_detail'),
    url(r'^(?P<product_id>\d+)', add_to_cart, name='add_to_cart'),  
    url(r'^(?P<category_name>[-\w]+)/$', products_list, name='products_list'),
]