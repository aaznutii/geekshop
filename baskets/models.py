from django.db import models

# Create your models here.

from auth_app.models import User
from  products.models import Product

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина пользователя {self.user.username} / Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(bas.sum() for bas in baskets)

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(bas.quantity for bas in baskets)