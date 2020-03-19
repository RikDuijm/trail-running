from django.contrib import admin
from .models import UserProfile, ProfilePost, ContactUser

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ProfilePost)
admin.site.register(ContactUser)
