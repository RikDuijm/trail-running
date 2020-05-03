from django.db import models
from django.utils import timezone


CATEGORY_CHOICES = (
    ("stories", "stories"),
    ("health_food", "health_food"),
    ("destinations", "destinations"),
    ("exercise_injuries", "exercise_injuries"),
)

class Article(models.Model):
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=30, default='')
    introduction = models.TextField()
    content_one = models.TextField(blank=True, null=True)	
    content_two = models.TextField(blank=True, null=True)	
    content_three = models.TextField(blank=True, null=True)	
    content_four = models.TextField(blank=True, null=True)	
    content_five = models.TextField(blank=True, null=True)	
    main_image = models.ImageField(upload_to="inspiration_images")
    image_one = models.ImageField(upload_to="inspiration_images", blank=True, null=True)
    image_two = models.ImageField(upload_to="inspiration_images", blank=True, null=True)
    image_three = models.ImageField(upload_to="inspiration_images", blank=True, null=True)
    image_four = models.ImageField(upload_to="inspiration_images", blank=True, null=True)
    image_five = models.ImageField(upload_to="inspiration_images", blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return "{0} - category {1} - by {2}".format(self.title, self.category, self.author)