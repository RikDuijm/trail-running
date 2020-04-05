from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def all_products(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, "products.html", {
        'category': category,
        'categories': categories,
        'products': products
        })


# def all_products(request):
#     products = Product.objects.all()
#     size_form = SizeForm()
#     size_model_form = SizeModelForm()

#     return render(request, "products.html", {
#         "products": products,
#         'size_form': size_form,
#         'size_model_form': size_model_form,
#     })

    
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request, "product/detail.html", {
        "product": product})
