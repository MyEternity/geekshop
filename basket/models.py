from django.db import models

from products.models import Product
from users.models import User


# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    @property
    def sum(self):
        return self.quantity * self.product.price

    @staticmethod
    def cp_total_sum(user):
        baskets = Basket.objects.filter(user=user)
        return sum(basket.sum for basket in baskets)

    @staticmethod
    def cp_total_qty(user):
        baskets = Basket.objects.filter(user=user)
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum for basket in baskets)

    def total_qty(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)
