from django.conf.urls import url, include
from .views import all_events

urlpatterns = [
    url(r'^$', all_events, name='all_events'),
]