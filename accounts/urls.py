from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, author_profile, profile_post
from accounts import url_reset



urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^yourprofile/$', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^profile/(?P<pk>\d+)', author_profile, name="author_profile"),    
    url(r'^new/$', profile_post, name='profile_post'),  # ?
    #url(r'^(?P<pk>\d+)/new/$', profile_post, name='profile_post'),
]