from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from discounts.models import Product


@login_required
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


@login_required
def add_to_cart(request, id):
    """View that adds items to the cart"""
    if request.user.is_authenticated:

        if request.POST.get('quantity') and int(request.POST.get('quantity')) > 0:  
            quantity = int(request.POST.get('quantity'))
            #SKU combines the product-id with different sizes. Model from Discouts App 
            sku_id =  (request.POST.get('sku'))    
            cart = request.session.get('cart', {})
            cart[sku_id] = int(cart.get(sku_id, 0)) + quantity
            request.session['cart'] = cart
            messages.warning(request, 'The product is added to your cart.')
        else:
            # Warning if the amount of products is not specified
            messages.warning(request, 'You have to specify how many products you want to purchase.')
    else:
        # Warning if the user is not logged in
        messages.warning(request, 'You have to log in / register first, before you can purchase our products.')
            
    return redirect(reverse('all_products'))


@login_required
def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    if request.user.is_authenticated:
        if request.POST.get('quantity') and int(request.POST.get('quantity')) > 0:
            quantity = int(request.POST.get('quantity'))
            cart = request.session.get('cart', {})
            if quantity > 0:
                cart[id] = quantity
            else:
                # pop() is an inbuilt function in Python that removes and returns last value from the list or the given index value. Syntax : list_name.pop(index)
                cart.pop(id)    
            request.session['cart'] = cart
        else:
            messages.warning(request, 'You have to specify how many products you want to purchase.')
    else:
        messages.warning(request, 'You have to register first, before you can purchase our products.')      
    return redirect(reverse('view_cart'))


@login_required
def delete_from_cart(request, id):
    cart = request.session.get('cart', {})
    if id in cart:
        del cart[id]
    request.session['cart'] = cart
    return redirect(reverse('view_cart')) 