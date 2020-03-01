from django.db import models
from django.utils import timezone

# Create your models here.

# class Month(models.Model):
#     name = models.CharField(max_length=254, default='')

#     def __str__(self):
#         return self.name


class Month(models.Model):
    name = models.CharField(max_length=255)

def __str__(self):
    return self.name


class Event(models.Model):
    name = models.CharField(max_length=254, default='')
    distance = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='events_images')
    month = models.ForeignKey('Month', default=0)

    def __str__(self):
        return self.name

        