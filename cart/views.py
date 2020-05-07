from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from discounts.models import Product


def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):

    if request.user.is_authenticated:

        if request.POST.get('quantity') and int(request.POST.get('quantity')) > 0:  
            quantity = int(request.POST.get('quantity')) 
            sku_id =  (request.POST.get('sku'))    
            cart = request.session.get('cart', {})
            
            cart[sku_id] = int(cart.get(sku_id, 0)) + quantity
            
            request.session['cart'] = cart

        else:
            messages.warning(request, 'You have to specify how many products you want to purchase.')
    else:
        messages.warning(request, 'You have to log in / register first, before you can purchase our products.')
            
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