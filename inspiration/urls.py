from django.conf.urls import url
from .views import get_articlesView, routes_destinationsView, article_detailView


urlpatterns = [
    url(r'^$', get_articlesView, name='get_articles'),
    url(r'^routes_destinations/$', routes_destinationsView, name='routes_destinationsView'),
    url(r'^(?P<pk>\d+)/$', article_detailView, name='article_detailView'),
]