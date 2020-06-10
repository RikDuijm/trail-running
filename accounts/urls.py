from django.conf.urls import url, include
from accounts.views import (
    logout, login, registration, profile_post, edit_profile,
    edit_profile_post, delete_profile_post, delete_profile_details, 
    deleted_user, author_profile, all_users, user_profile_page, user_profile, 
    contact_user, search_user_first_name, search_user_last_name,
    search_user_location, delete_personal_message
)
from accounts import url_reset

urlpatterns = [
    url(r'^users/$', all_users, name="all_users"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^yourprofile/$', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^profile/(?P<pk>\d+)', author_profile, name="author_profile"), 
    url(r'^userprofiles/(?P<pk>\d+)', user_profile_page, name="user_profile_page"),
    url(r'^newprofilepost/$', profile_post, name='profile_post'),  
    url(r'^contactuser/(?P<pk>\d+)', contact_user, name='contact_user'),
    url(r'^editprofile/$', edit_profile, name='edit_profile'),
    url(r'^deleteprofile/', delete_profile_details, name='delete_profile_details'),
    url(r'^deleted-user/', deleted_user, name='deleted_user'),
    url(r'^(?P<pk>\d+)/edit/$', edit_profile_post, name='edit_profile_post'),
    url(r'^(?P<pk>\d+)/delete/$', delete_profile_post, name='delete_profile_post'),
    url(r'^(?P<pk>\d+)/delete-message/$', delete_personal_message, name='delete_personal_message'),
    url(r'^(?P<pk>\d+)/new/$', profile_post, name='profile_post'),
    url(r'^user-search-firstname/$', search_user_first_name, name='search_user_first_name'),
    url(r'^user-search-lastname/$', search_user_last_name, name='search_user_last_name'),
    url(r'^user-search-location/$', search_user_location, name='search_user_location')

]