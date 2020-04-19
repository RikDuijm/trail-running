from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
# from django.http import HttpResponse, JsonResponse
# from django.contrib import messages

from discounts.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.

def cart_detail(request):
    """A View that renders the cart contents page"""
    cart = Cart(request)
    return render(request, "cart.html", {'cart': cart})

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    # get product object by id
    product = get_object_or_404(Product, id=product_id)
    # get selected size from request data
    # size = request.POST['size']
    form = CartAddProductForm(request.POST)
    

    if request.user.is_authenticated and form.is_valid():
        # add product to the cart
        # or update it's quantity/ size
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])  # size=size, 
        
  
    return redirect('cart:cart_detail')


def delete_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


        # if updated_cart:
        #     # if cart updated return success status
        #     subtotal_price = cart.get_subtotal_price()
        #     delivery_price = cart.get_delivery_price()
        #     total_price = cart.get_total_price()
        #     data = {
        #         'size': size,
        #         'subtotal_price': subtotal_price,
        #         'total_price': total_price
        #     }
        #     return JsonResponse(data, status=200)   # 
        # else:
        #     # if cart not updated return error message
        #     return HttpResponse(status=400)

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        # create form for each item in the cart
        # to allow updating its quantity and size
        item['update_quantity_form'] = CartForm(initial={'quantity': item['quantity'],'update': True})
    args = {'cart': cart}
    return render(request, 'cart/cart.html', args)
    

    #     if request.POST.get('quantity') and int(request.POST.get('quantity')) > 0:
    #         quantity = int(request.POST.get('quantity')) 
    #         # if request.POST.get('size'):
    #         #     size = int(request.POST.get('size'))
    #         #     print(size)

    #         cart = request.session.get('cart', {})
    #         size = int(request.POST.get('size'))
            
    #         if id in cart:
    #             cart[id] = int(cart[id]) + quantity
    #             print("in if")
    #             print(size)
    #         else:
    #             cart[id] = cart.get(id, quantity)
                
    #             print("in else")
    #             print(size)
    #         request.session['cart'] = cart
    #     else:
    #         messages.warning(request, 'You have to specify how many products you want to purchase.')
    # else:
    #     messages.warning(request, 'You have to log in / register first, before you can purchase our products.')
            
    # return redirect(reverse('products_list'))

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


