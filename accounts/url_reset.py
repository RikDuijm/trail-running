from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    # Create a post reset redirect which redirects to the password reset done view.
    url('^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),  
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
        # create a uidb64 which is made up of numbers from 0 to 9 and  letters A-Z and lowercase a-z. 
        # After that the token will be the unique URL for any user that tries to reset their password 
        # This links them to password reset confirm page and this is the URL that would be sent in an email.
    url('^complete/$', password_reset_complete, name='password_reset_complete')
]