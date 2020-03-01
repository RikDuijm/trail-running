from django.conf.urls import url, include
from .views import Calendar

urlpatterns = [
    url(r'^$', Calendar.as_view(), name='all_events'),
]