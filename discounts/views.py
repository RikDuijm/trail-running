from django.shortcuts import render
from .models import Product
from .forms import SizeForm  # SizeModelForm, 

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    size_form = SizeForm()
    # size_model_form = SizeModelForm()

    return render(request, "products.html", {
        "products": products,
        'size_form': size_form,
        # 'size_model_form': size_model_form,
    })
