from __future__ import unicode_literals
from decimal import *
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Product, Size, Stock
from cart.forms import CartAddProductForm

def products_list(request, category_name=None):
    selected_categories = None
    products = Product.objects.all()
    categories = Category.objects.all()
    sizes = Size.objects.all()

    return render(request, "products.html", {
        'sizes': sizes,
        'categories': categories,
        'products': products
        })


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    sizes = product.size.all()
    
    cart_form = CartAddProductForm()                     

    args = {'product': product, 'sizes': sizes, 'cart_form': cart_form}

    return render(request, 'product.html', args)