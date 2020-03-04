from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.

def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

def add_to_cart(request, id):
    if request.user.is_authenticated:
        """Add a quantity of the specified product to the cart"""
        if request.POST.get('quantity') and int(request.POST.get('quantity')) > 0:
            quantity = int(request.POST.get('quantity'))

            """First step, check to see if quantity is NOT null (or whatever an empty value comes back as"""
            """ If not an empty field, then run the code below as normal, else (go to line 30)  """

            """This takes an integer, and this gets an integer from the the form in Discounts/products.html.
            That allow  to increase and decrease the number of items the client wants.
            And when he clicks on the Add to Cart button, the integer that is in that form will go to the cart."""

            cart = request.session.get('cart', {})  # request.session means it's not going to a database. It gets a cart from the session, if one already exists or an empty dictionary if a cart doesn't exist yet.
            if id in cart:
                cart[id] = int(cart[id]) + quantity  # If product is already in cart, add the new order to it, instead of overwriting first order.
            else:     
                cart[id] = cart.get(id, quantity)       # Add an ID and a quantity.

            request.session['cart'] = cart
        else:
            messages.warning(request, 'You have to specify how many products you want to purchase.')
    else:
            messages.warning(request, 'You have to register first, before you can purchase our products.')
            
    return redirect(reverse('all_products'))

def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    if request.user.is_authenticated:
        
        if request.POST.get('quantity') and int(request.POST.get('quantity')) > 0:
            quantity = int(request.POST.get('quantity'))
            cart = request.session.get('cart', {})

            if quantity > 0:
                cart[id] = quantity
            else:
                cart.pop(id)    # pop() is an inbuilt function in Python that removes and returns last value from the list or the given index value. Syntax : list_name.pop(index)

            request.session['cart'] = cart
        else:
            messages.warning(request, 'You have to specify how many products you want to purchase.')

    else:
           
            messages.warning(request, 'You have to register first, before you can purchase our products.')
            
    return redirect(reverse('view_cart'))

def delete_from_cart(request, id):
    cart = request.session.get('cart', {})
    if id in cart:
        del cart[id]
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))        

        