from django.shortcuts import render, get_object_or_404
from .models import Product, SKU

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


