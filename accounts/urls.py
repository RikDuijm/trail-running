from django.conf.urls import url, include
from accounts.views import logout

urlpatterns = [
url(r'^accounts/logout/$', logout, name="logout")
]