from rest_framework import serializers

from .models import Cart, CartItem, Order
from items.models import Item
from items.serializers import ItemSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ItemSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(),
        source='product',
        write_only=True,
    )

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_item = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'user', 'created', 'cart_item')

    def get_cart_item(self, obj):
        cart_items = obj.cart_item.all().order_by('created')
        serializer = CartItemSerializer(instance=cart_items, many=True)
        return serializer.data


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
