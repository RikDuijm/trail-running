from __future__ import unicode_literals
from django.contrib import admin
from .models import Product, Category, Size, Stock

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'created_date']
    list_filter = ['category__category', 'size__size', 'created_date']


admin.site.register(Product, ProductAdmin)


class SizeAdmin(admin.ModelAdmin):
    list_display = ['size']


admin.site.register(Size, SizeAdmin)


class StockAdmin(admin.ModelAdmin): 
    list_display = ['amount', 'product', 'size']
    list_filter = ['product__product_name', 'size__size']


admin.site.register(Stock, StockAdmin)