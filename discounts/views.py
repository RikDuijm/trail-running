from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product, SKU

# Create your views here.
def all_products(request):
    """
    Create a view that will return a list of Products, 
    ordered them by using the published date and render them to the 'products.html' template
    """
    products = Product.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date').all()
    
    return render(request, "products.html", {"products": products})

