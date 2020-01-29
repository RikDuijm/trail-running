from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    """This takes an integer, and this gets an integer from the the form in Discounts/products.html.
    That allow  to increase and decrease the number of items the client wants.
    And when he clicks on the Add to Cart button, the integer that is in that form will go to the cart."""

    cart = request.session.get('cart', {})  # request.session means it's not going to a database. It gets a cart from the session, if one already exists or an empty dictionary if a cart doesn't exist yet.
    cart[id] = cart.get(id, quantity)       # Add an ID and a quantity.

    request.session['cart'] = cart
    return redirect(reverse('all_products'))

def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)    # pop() is an inbuilt function in Python that removes and returns last value from the list or the given index value. Syntax : list_name.pop(index)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))