from django.contrib.auth import get_user_model
from django.db import models

from items.models import Item

User = get_user_model()


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_cart')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина пользователя {self.user}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='product_item')
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_orders')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='order')
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Заказ пользователя {self.user}'
