from django.db import models
from django.utils import timezone

SIZE_CHOICES = (
    ('xxs', 'XX-Small'),
    ('xs', 'X-Small'),
    ('s', 'Small'),
    ('m', 'Medium'),
    ('l', 'Large'),
    ('xl', 'X-Large'),
    ('xxl', 'XX-Large'),
    ("35", "35"),
    ("36", "36"),
    ("37", "37"),
    ("38", "38"),
    ("39", "39"),
    ("40", "40"),
    ("41", "41"),
    ("42", "42"),
    ("43", "43"),
    ("44", "44"),
    ("45", "45"),
    ("46", "46"),
    ("47", "47"),
)


class Size(models.Model):
    size = models.CharField(
        max_length=3,
        choices=SIZE_CHOICES,
        default='n/a'
        ) 
    def __str__(self):
        return self.size


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
    sizes = models.ManyToManyField(Size, through='Item')
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


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} (size {1})".format(self.product, self.size)

        
















# SHOE_SIZE_CHOICES = ( 
#     ("35", "35"), 
#     ("36", "36"),
#     ("37", "37"), 
#     ("38", "38"), 
#     ("39", "39"), 
#     ("40", "40"), 
#     ("41", "41"), 
#     ("42", "42"),
#     ("43", "43"),
#     ("44", "44"),
#     ("45", "45"),
#     ("46", "46"),
#     ("47", "47"),                     
# ) 

# TYPE_CHOICES = (
#     ("watches","watches"),
#     ("clothes","clothes"),
#     ("shoes","shoes"),
#     ("events","events"),
# )

# class Product(models.Model):
    # product_name = models.CharField(max_length=254, default='')
    # product_type = models.CharField(
    #     max_length=10,
    #     choices=TYPE_CHOICES,
    #     default="shoes") 
    # description = models.TextField(null=True)
    # normal_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    # created_date = models.DateTimeField(auto_now_add=True)
    # published_date = models.DateTimeField(blank=True, null=True,
    #                                       default=timezone.now)
    # valid_until = models.DateTimeField(blank=True, null=True, default=timezone.now)                                     
    # views = models.IntegerField(default=0)
    # image = models.ImageField(upload_to="product_images", blank=True, null=True)
    # shoe_size = models.CharField(
    #     max_length=2,
    #     choices=SHOE_SIZE_CHOICES,
    #     default='35'
    #     ) 


    # def __str__(self):
    #     return self.product_name