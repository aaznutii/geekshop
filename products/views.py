from django.shortcuts import render
from products.models import Product, ProductCategory
from django.views.generic import DetailView
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


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/datail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
