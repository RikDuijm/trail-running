from django.shortcuts import render
from discounts.models import Product

def search_product(request):
    products = Product.objects.filter(product_name__icontains=request.GET['query'])
    return render(request, "products.html", {"products": products})
