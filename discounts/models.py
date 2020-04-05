from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('all_products', kwargs={'id': self.id, 'slug': self.slug })


class Size(models.Model):
    size = models.CharField(max_length=20)

    class Meta:
        ordering = ('size', )

    def __unicode__(self):
        return self.size


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=254, db_index=True) 
    slug = models.SlugField(max_length=200, null=True, db_index=True)
    image = models.ImageField(upload_to="product_images", blank=True, null=True)
    description = models.TextField(null=True)  
    normal_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.ManyToManyField('Size')
    available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    valid_until = models.DateTimeField(blank=True, null=True, default=timezone.now)                                    

    class Meta: 
        ordering = ('product_name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'id': self.id, 'slug': self.slug })