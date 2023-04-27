from django.contrib import admin
from .models import Cart, CartItem


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'created',
    )

@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'cart',
        'product',
        'quantity',
        'created'
    )