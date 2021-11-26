from django.shortcuts import render
from products.models import Product, ProductCategory
# Create your views here.


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Geekshop | Каталог',}

    context['products'] = Product.objects.all()
    context['productcategory'] = ProductCategory.objects.all()
    return render(request, 'products/products.html', context)

