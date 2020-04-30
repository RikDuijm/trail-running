from django.conf.urls import url
from .views import get_articlesView, article_detailView

urlpatterns = [
    url(r'^$', get_articlesView, name='get_articles'),
    url(r'^(?P<pk>\d+)/$', article_detailView, name='article_detail'),
]