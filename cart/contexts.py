from django.shortcuts import get_object_or_404
from discounts.models import Product

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})                      # requests the existing cart if there is one, or a blank dictionary if there's not.

    cart_items = []                                             # initialize cart_items, total, and product_count.
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():                           # product ID, quantity= how many the user wishes to purchase
        product = get_object_or_404(Product, pk=id)             # product is from the product model in Discounts. 
                                                                # Use the primary key as ID, as every product within database will have a primary key, which is a unique ID.
        total += quantity * product.price                       # Total = the quantity of items multiplied by their price and add them to a continuous running total of the cost.
        product_count += quantity                               #  product_count keeps on adding the quantity. So as a user adds more quantity ,the product count goes up.

        cart_items.append({'id': id, 'quantity': quantity, 'product': product}) # Append those cart_items to the cart. The unique ID of each product and the quantity of that product that has been added.
    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count} # return key value pairs for cart_items, total, and product_count.

