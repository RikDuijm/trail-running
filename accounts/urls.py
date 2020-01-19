from django.conf.urls import url, include
from accounts.views import logout, login

urlpatterns = [
url(r'^accounts/logout/$', logout, name="logout"),
url(r'^accounts/login/$', login, name="login"),
]