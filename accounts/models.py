from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

gender_choices = (
    ('optional', 'does it mattter?'),
    ('male', 'male'),
    ('female', 'female'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)       # Make sure that one user only has one profile
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=10,
                              choices=gender_choices,
                              default='optional')
    age = models.IntegerField()
    location = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='profile_images', blank=True)

    def __str__ (self):
        return self.user.username

class ProfileIntroduction(models.Model):
    introduction = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.introduction
 