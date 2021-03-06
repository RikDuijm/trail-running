from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import UserProfile

class Post(models.Model):
    """
    A single Blog post
    """
    author = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)                           
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return "{0} (by {1})".format(self.title, self.author)