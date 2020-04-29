from django.conf.urls import url
from .views import view_cart, adjust_cart, delete_from_cart, add_to_cart   # , add_size_quantity

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    # url(r'^test$', add_size_quantity, name='add_size_quantity'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    url(r'^delete/(?P<id>\d+)', delete_from_cart, name='delete_from_cart'),
]