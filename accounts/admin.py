from django.contrib import admin
from .models import UserProfile, ProfilePost

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ProfilePost)