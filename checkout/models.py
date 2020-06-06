from django.db import models
from discounts.models import Product, SKU


gender_choices = (
    ('optional', 'Fill out when you participate in a race'),
    ('male', 'male'),
    ('female', 'female'),
)

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    gender = gender = models.CharField(max_length=10,
                                       choices=gender_choices,
                                       default='optional')
    age = models.IntegerField(blank=True, default=0)                          
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postal_code = models.CharField(max_length=20, blank=True)
    home_town = models.CharField(max_length=40, blank=False)
    street_address = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    sku = models.ForeignKey(SKU, null=True)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.sku.product.product_name, self.sku.product.price)