from django.shortcuts import render
from products.models import Product
# Create your views here.


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    # data = get_cards()['cards']
    data = Product.objects.all()
    context = {
        'title': 'geekshop',
        'cards': data
    }
    return render(request, 'products/products.html', context)

