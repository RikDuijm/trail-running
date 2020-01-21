from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url('^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'), # Create a post reset redirect which redirects to the password reset done view.
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
        # create a uidb64 and that uid is going to be made up of numbers from 0 to 9 and then letters a capital A-Z and lowercase a-z. 
        # After that we're going to have our token and this will be the unique URL that would be given to any user that tries to reset their password 
        # and this is going to link them to the URL set a password reset confirm page and this is usually the URL that would be sent in an email.
    url('^complete/$', password_reset_complete, name='password_reset_complete')
]