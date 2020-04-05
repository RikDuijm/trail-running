from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'slug', 'normal_price', 'price', 'available', 'created_date', 'updated']
    list_filter = ['available', 'created_date', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('product_name',)}
