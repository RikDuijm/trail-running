from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.

gender_choices = (
    ('optional', 'does it mattter?'),
    ('male', 'male'),
    ('female', 'female'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)       
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=10,
                              choices=gender_choices,
                              default='optional')
    age = models.IntegerField()
    location = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='profile_images', blank=True, unique=True)

#    def __str__ (self):            Error in admin environment when I return string....
#        return self.user

class ProfilePost(models.Model):
    user = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT) 
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    image = models.ImageField(upload_to="profile_images", blank=True, null=True)
    
    def __unicode__(self):
        return self.title