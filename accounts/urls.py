from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, profile_post, author_profile, all_users, user_profile_page  #, get_profile_posts 
from accounts import url_reset

urlpatterns = [
    url(r'^users/$', all_users, name="all_users"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^yourprofile/$', user_profile, name="profile"),
 #   url(r'^test/$', get_profile_posts, name='get_profile_posts'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^profile/(?P<pk>\d+)', author_profile, name="author_profile"), # url for Community / Forum    
    url(r'^profile/(?P<pk>\d+)', user_profile_page, name="user_profile_page"),
    url(r'^newprofilepost/$', profile_post, name='profile_post'),  # ?
    #url(r'^(?P<pk>\d+)/new/$', profile_post, name='profile_post'),
]