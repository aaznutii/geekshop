
import json
from django.core.management.base import BaseCommand
from products.models import Product, ProductCategory
import datetime



# def write_json(date):
#     with open(file_name, mode='w', encoding='utf8') as infile:
#         json.dumps()
#
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         categories = load_from_json('products/fixtures/categories.json')
#
#         ProductCategory.objects.all().delete()
#         for category in categories:
#             cat = category.get('fields')
#             cat['id'] = category.get('pk')
#             new_category = ProductCategory(**cat)
#             new_category.save()
#
#         products = load_from_json('products/fixtures/products.json')
#
#         Product.objects.all().delete()
#         for product in products:
#             prod = product.get('fields')
#             category = prod.get('category')
#             _category = ProductCategory.objects.get(id=category)
#             prod['category'] = _category
#             new_category = Product(**prod)
#             new_category.save()
