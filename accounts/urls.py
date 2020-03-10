from django.conf.urls import url, include
from accounts.views import (
    logout, login, registration, profile_post, edit_profile,
    edit_profile_post, delete_profile_post, delete_profile_details,
    author_profile, all_users, user_profile_page, user_profile, contact_user,
    search_user
    # get_profile_posts
)
from accounts import url_reset

urlpatterns = [
    url(r'^users/$', all_users, name="all_users"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^yourprofile/$', user_profile, name="profile"),
    # url(r'^test/$', get_profile_posts, name='get_profile_posts'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^profile/(?P<pk>\d+)', author_profile, name="author_profile"), # url for Community / Forum    
    url(r'^userprofiles/(?P<pk>\d+)', user_profile_page, name="user_profile_page"),
    url(r'^newprofilepost/$', profile_post, name='profile_post'),  # ?
    url(r'^contactuser/$', contact_user, name='contact_user'),
    url(r'^editprofile/$', edit_profile, name='edit_profile'),
    url(r'^deleteprofile/', delete_profile_details, name='delete_profile_details'),
    url(r'^(?P<pk>\d+)/edit/$', edit_profile_post, name='edit_profile_post'),
    url(r'^(?P<pk>\d+)/delete/$', delete_profile_post, name='delete_profile_post'),
    # url(r'^(?P<pk>\d+)/new/$', profile_post, name='profile_post'),
    url(r'^user-search/$', search_user, name='search_user')

]