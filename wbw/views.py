from django.shortcuts import render

from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'wbw/product_list.html', {'products': products})
