from .cart import Cart
#  documentation: https://docs.djangoproject.com/en/1.11/ref/templates/api/


def cart(request):
    return {'cart': Cart(request)}