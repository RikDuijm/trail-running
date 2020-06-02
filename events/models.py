from django.db import models
from django.utils import timezone

# Create your models here.

# class Month(models.Model):
#     name = models.CharField(max_length=254, default='')

#     def __str__(self):
#         return self.name


class Event(models.Model):
    day_of_month = models.IntegerField(null=False)
    name = models.CharField(max_length=254, default='')
    distance = models.CharField(max_length=254, default='')
    distance_range = models.CharField(max_length=254, default='')
    normal_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    valid_until = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    description = models.TextField() 
    image = models.ImageField(upload_to='events_images')
    month = models.CharField(max_length=254, default='')
    region = models.CharField(max_length=254, default='')
    def __str__(self):
        return self.name

        