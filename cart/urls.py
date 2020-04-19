from django.conf.urls import url
from .views import cart_detail, add_to_cart, delete_from_cart  # , adjust_cart , 

urlpatterns = [
    url(r'^$', cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)', add_to_cart, name='add_to_cart'),  
#    url(r'^adjust/(?P<product_id>\d+)', adjust_cart, name='adjust_cart'),
    url(r'^delete/(?P<product_id>\d+)', delete_from_cart, name='delete_from_cart'),
]