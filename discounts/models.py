from django.db import models

from django.utils import timezone



class Size(models.Model):
    name = models.CharField(max_length=30)
    # parent = models.ForeignKey('Size', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


TYPE_CHOICES = (
    ("watches", "watches"),
    ("clothes", "clothes"),
    ("shoes", "shoes"),
    ("events", "events"),
)


class Product(models.Model):
    product_name = models.CharField(max_length=254, default='')
    product_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default="shoes")
    # size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    normal_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    valid_until = models.DateTimeField(blank=True, null=True, default=timezone.now)                                    
    image = models.ImageField(upload_to="product_images", blank=True, null=True)

    def __str__(self):
        return self.product_name
