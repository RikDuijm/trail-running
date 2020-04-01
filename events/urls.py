from django.conf.urls import url, include
from .views import ( 
    all_events, search_race_name, search_race_month, search_race_distance, 
    search_race_region
)


urlpatterns = [
    url(r'^$', all_events, name='all_events'),
    url(r'^event-search-racename/$', search_race_name, name='search_race_name'),
    url(r'^event-search-month/$', search_race_month, name='search_race_month'),
    url(r'^event-search-distance/$', search_race_distance, 
        name='search_race_distance'),
    url(r'^event-search-region/$', search_race_region, name='search_race_region'),
]