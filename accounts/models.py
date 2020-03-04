from django.conf import settings
from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone


gender_choices = (
    ('optional', 'does it mattter?'),
    ('male', 'male'),
    ('female', 'female'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)       
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True)
    gender = models.CharField(max_length=10,
                              choices=gender_choices,
                              default='optional')
    age = models.IntegerField()
    location = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='profile_images', blank=True, unique=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class ProfilePost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, default=1, on_delete=models.SET_DEFAULT) 
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    image = models.ImageField(upload_to="profile_images", blank=True, null=True)
    
    def __str__(self):
        return "{0} (by {1})".format(self.title, self.user)