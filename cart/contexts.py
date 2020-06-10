from django.shortcuts import get_object_or_404
from discounts.models import Product, SKU

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})                      
    cart_items = []                                             
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        sku = get_object_or_404(SKU, pk=id)
        total += quantity * sku.product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'sku': sku}) 
        
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count} 