"""django_trailrunning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views import static
from .settings import MEDIA_ROOT
from accounts import urls as accounts_urls
from discounts import urls as urls_discounts
from accounts.views import index
from cart import urls as urls_cart


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^$', index, name='index'),
    url(r'^home/', include('home.urls')),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^community/', include('community.urls')),
    url(r'^discounts/', include(urls_discounts)),
    url(r'^cart/', include(urls_cart)),
]