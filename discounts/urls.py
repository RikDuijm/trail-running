from django.conf.urls import url, include
from .views import all_products, product_detail


urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url('(?P<category_slug>[-\w]+)/$', all_products, name='all_products'),
    url('(?P<slug>[-\w]+)/(?P<pk>\d+)/$', product_detail, name='product_detail'),
]