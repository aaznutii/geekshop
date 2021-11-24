
import json
from django.core.management.base import BaseCommand
from products.models import Product, ProductCategory


def load_from_json(file_name):
    # Получение данных из файлов json
    with open(file_name, mode='r', encoding='utf8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    # Загрузка данных в базу данных из json команда: py -3 .\manage.py fill_db
    def handle(self, *args, **options):
        categories = load_from_json('products/fixtures/main_products_productcategory.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategory(**cat)
            new_category.save()

        products = load_from_json('products/fixtures/main_products_product.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ProductCategory.objects.get(id=category)
            prod['category'] = _category
            new_category = Product(**prod)
            new_category.save()
