from django.conf.urls import url
from .views import get_posts, post_detail, new_post

urlpatterns = [
url(r'^$', get_posts, name='get_posts'),
url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
url(r'^new/$', new_post, name='new_post'),

]