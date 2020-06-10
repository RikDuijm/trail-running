from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from discounts.models import Product, SKU
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


# When user goes to the checkout  to pay, he should be logged in.
@login_required()                                               
# The user is given the order form to fill out. 
# This form contains their name, address, and so on. 
# The payment form contains the credit card or debit card details. Imported from forms.py.
def checkout(request):
    if request.method == "POST":                                
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        # If the order form and the payment form are valid (filled out correctly) the order form will be saved as order.
        if order_form.is_valid() and payment_form.is_valid():   
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            # Get the information about what is being purchased from the cart from the current session.
            cart = request.session.get('cart', {})              
            # Initialize a total of 0 and then do a for loop. Go over ID and quantity in the cart_items. From that, we get the product.
            total = 0                                           
            for id, quantity in cart.items():
                # Get the Product ID. To get the total,  add a quantity multiplied by product price.
                sku = get_object_or_404(SKU, pk=id)     
                total += quantity * sku.product.price    
                # OrderLineItem. takes the things just created: order, product, quantity. Save it and we have the details of the order.           
                order_line_item = OrderLineItem(            	
                    order=order,
                    sku=sku,
                    quantity=quantity
                )
                order_line_item.save()

            """Now that the purchase is defined, a try except will create a customer charge. It's using Stripe's in-built API. 
                Give it an amount of money that we wish. That's an integer. And it's the total * 100 because Stripe uses everything in cents or pennies."""
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,            
                    # The description is going to be the request user email to see from the Stripe dashboard from whom the payment came. 
                    card=payment_form.cleaned_data['stripe_id']  # The Stripe ID from that form - that's the item that was hidden from the user.
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.error(request, "Thanks for your preference. You have successfully paid. We'll send you a confirmation of your purchase within one working day.")
                request.session['cart'] = {}
                return redirect(reverse('all_products'))
            else:                                              
                messages.error(request, "Unable to take payment")
        else:       
            # Else for the previous if loop. It will print any payment form errors and the message.
            print(payment_form.errors)                          
            messages.error(request, "We were unable to take a payment with that card!")
            print("Your card was declined!")
    else:
        # The else for the outermost loop. Returns a blank form.
        payment_form = MakePaymentForm()                        
        order_form = OrderForm()
    # Return the checkout HTML. And within that,  include an order form, a payment form, and a publishable key for Stripe. 
    return render(request, "checkout.html", {
                    "order_form": order_form, 
                    "payment_form": payment_form, 
                    "publishable": settings.STRIPE_PUBLISHABLE})