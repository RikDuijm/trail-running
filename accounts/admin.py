from django.contrib import admin
from .models import UserProfile, ProfileIntroduction

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ProfileIntroduction)