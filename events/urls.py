from django.conf.urls import url, include
from .views import all_events, events_ordered_by_date

urlpatterns = [
    url(r'^$', all_events, name='all_events'),
    url(r'^test$', events_ordered_by_date, name='events_ordered_by_date'),
]