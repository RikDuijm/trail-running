from django.contrib import admin
from .models import Product, Item, Size

# Register your models here.
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Size)