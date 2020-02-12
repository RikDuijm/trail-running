from django.conf.urls import url, include
from .views import all_products, test



urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^test/$', test, name="test"),
]