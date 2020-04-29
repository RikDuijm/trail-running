# from decimal import Decimal

# from django.conf import settings
# from django.shortcuts import get_object_or_404
# from discounts.models import Product, ClothesSize, ShoeSize

# # class created following instructions by Antonio Mele
# # in the book Django By Example
# class Cart(object):
#     def __init__(self, request):
#         # initialize the cart
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             # save an empty cart in the session
#             cart = self.session[settings.CART_SESSION_ID] = {}  # []
#         self.cart = cart

    
#     def add(self, product, quantity=1, update_quantity=False):  # , size?       
#         # add product to the cart or update its quantity/size
#         # size = product.size.filter(size=size)
#         product_id = str(product.id)
#         if product_id not in self.cart:
#             self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
#         if update_quantity:
#             self.cart[product_id]['quantity'] = quantity
#         else:
#             self.cart[product_id]['quantity'] += quantity
#         self.save

#     def save(self):
#         # mark the session as "modified" to make sure it gets saved.
#         self.session.modified = True

#     def remove(self, product):
#         # remove a product from the cart
#         product_id = str(product.id)
#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save

#     def __iter__(self):
#         # iterate over the items in the cart and get the products from the database.
#         product_ids = self.cart.keys()
#         # get the product objects and add them to the cart
#         products = Product.object.filter(id__in=product_ids)

#         cart = self.cart.copy()
#         for product in products:
#             cart[str(product.id)['product']] = product

#         for item in cart.values():
#             item['price'] = Decimal(item['price'])
#             item['total_price'] = item ['price'] * item ['quantity']
#             yield item

#     def __len__(self):
#         # count all items in the cart
#         return sum(item['quantity'] for item in self.cart.values())        

#     def get_total_price(self):
#         return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

#     def clear(self):
#         # remove cart from session
#         del self.session[settings.CART_SESSION_ID]
#         self.save



#     # def remove(self, product_id, size):
#     # # remove the product from the cart
#     #     for item in self.cart:
#     #         if item['product_id'] == product_id and str(item['size']) == size:
#     #             self.cart.remove(item)
#     #     self.save()

#     # def __iter__(self):
#     #     # iterate over the items in the cart and get the products from the database
#     #     for item in self.cart:
#     #         # get product
#     #         product = get_object_or_404(Product, pk=int(item['product_id']))
#     #         item['product'] = product
#     #         # get all product sizes
#     #         item['all_sizes'] = product.size.all()

#     #         # # get available sizes for the product, remove duplicates and sort by size field
#     #         # item['sizes_available'] = sorted(set([s.size for s in stock]), key=lambda k: k.size)
#     #         item['price'] = Decimal(item['price'])
#     #         item['total_price'] = item['price'] * item['quantity']
#     #         yield item

#     # def __len__(self):
#     #     # count all items in the cart
#     #     return sum(item['quantity'] for item in self.cart)

#     # def get_subtotal_price(self):
#     #     return '{0:.2f}'.format(sum(Decimal(item['price']) * item['quantity'] for item in self.cart))

#     # def get_delivery_price(self):
#     #     if Decimal(self.get_subtotal_price()) > Decimal(75.00):
#     #         return '{0:.2f}'.format(0)
#     #     else:
#     #         return '{0:.2f}'.format(2.95)

#     # def get_total_price(self):
#     #     return '{0:.2f}'.format(Decimal(self.get_subtotal_price()) + Decimal(self.get_delivery_price()))

#     # def clear(self):
#     #     # remove cart from session
#     #     del self.session[settings.CART_SESSION_ID]
#     #     self.session.modified = True    

#         # if self.cart:
#         #     for item in self.cart:
#         #         if item['product_id'] == str(product.id) and item['size'] == size:
#         #             if update:
#         #                 # if product and size is in the list and it is update request
#         #                 # update quantity
#         #                     item['quantity'] = quantity
#         #             else:
#         #                 # if product and size is in the list and same product and size added
#         #                 # increase quantity by one
#         #                     item['quantity'] += 1
#         #             self.save()
#         #             return True        

#         #     for item in self.cart:
#         #         if item['product_id'] == str(product.id):
#         #             if update:
#         #                 # if product is in the list and it is update request
#         #                 # change size
#         #                 item['size'] = size
#         #                 # update quantity
#         #                 item['quantity'] = quantity
#         #             else:
#         #                 # if product is in the list and same product added with different size
#         #                 # add new size
#         #                 self.cart.append(new_product)
#         #             self.save()
#         #             return True

#         #     for item in self.cart:
#         #         # if product is not in the cart add it
#         #         if item['product_id'] != str(product.id):
#         #             self.cart.append(new_product)
#         #             self.save()
#         #             return True

#         # else:
#         #     # if there are no items in the cart, add product
#         #     self.cart.append(new_product)
#         #     self.save()
#         #     return True

#     # def save(self):
#     #     # update the session cart
#     #     self.session[settings.CART_SESSION_ID] = self.cart
#     #     # mark the session as "modified" to make sure it is saved
#     #     self.session.modified = True

