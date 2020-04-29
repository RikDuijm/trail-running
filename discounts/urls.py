from django.conf.urls import url, include
from .views import all_products

urlpatterns = [
    url(r'^$', all_products, name='all_products'),
]


# urlpatterns = [
#     url(r'^$', products_list, name='products_list'),
#     url(r'^(?P<product_id>\d+)/$', product_detail, name='product_detail'),
#     url(r'^(?P<product_id>\d+)', add_to_cart, name='add_to_cart'),  
#     url(r'^(?P<category_name>[-\w]+)/$', products_list, name='products_list'),
# ]