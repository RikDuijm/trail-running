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
    first_name = models.CharField(max_length=30, null=True, blank=False)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    repeat_email = models.EmailField(max_length=99, null=True, blank=False)
    gender = models.CharField(max_length=10,
                              choices=gender_choices,
                              default='optional')
    age = models.IntegerField(blank=False)
    location = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to='profile_images', blank=True)
    about_me = models.TextField(max_length=1000, blank=True, null=True)
 
    def __str__(self):
        return f"{self.user.username}'s Profile"

class ProfilePost(models.Model):
    user = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(null=True, default=timezone.now)
    image = models.ImageField(upload_to="personal_messages", blank=True, null=True)
    
    def __str__(self):
        return "{0} (by {1})".format(self.title, self.user)

class ContactUser(models.Model):
    sender = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(null=True, default=timezone.now)
    image = models.ImageField(upload_to="profile_images", blank=True, null=True)
    recipient = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT, related_name="recipient")
    

    def __str__(self):
        return "{0} (by {1})".format(self.title, self.sender)
