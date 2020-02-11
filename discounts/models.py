from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=254, default='')
    description_introduction = models.TextField(null=True)
    description_first = models.TextField(null=True,)
    description_second = models.TextField(null=True,)
    description_third = models.TextField(null=True, blank=True)
    normal_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    valid_until = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)                                     
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="product_images", blank=True, null=True)


    def __str__(self):
        return self.product_name