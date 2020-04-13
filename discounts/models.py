from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    category = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ['category']

    def __unicode__(self):
        return self.category


class Size(models.Model):
    size = models.CharField(max_length=20)

    class Meta:
        ordering = ['size']

    def __unicode__(self):
        return self.size


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=60, db_index=True) 
    image = models.ImageField(upload_to="product_images", blank=True, null=True)
    description = models.TextField(null=True)  
    normal_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.ManyToManyField('Size')
    available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField(blank=True, null=True, default=timezone.now)                                    

    class Meta:
        ordering = ['product_name']

    def __unicode__(self):
        return self.product_name


class Stock(models.Model):
    amount = models.PositiveIntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)

    unique_together = ('product', 'size')