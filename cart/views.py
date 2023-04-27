from django.http import JsonResponse
from rest_framework import generics

from .models import Cart, CartItem, Order
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer
from .utils.initiate_payment import initiate_payment


# Create your views here.
class CartView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class CartItemView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def perform_create(self, serializer):
        product = serializer.validated_data.get('product')
        cart = serializer.validated_data.get('cart')
        quantity = serializer.validated_data.get('quantity', 1)
        cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def perform_update(self, serializer):
        quantity = serializer.validated_data.get('quantity', None)
        instance = self.get_object()

        if quantity is not None:
            instance.quantity = max(0, instance.quantity - quantity)
        else:
            instance.quantity -= 1

        if instance.quantity == 0:
            instance.delete()
        else:
            instance.save()


class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        cart = serializer.validated_data.get('cart')
        total_price = serializer.validated_data.get('total_price')
        order = Order.objects.create(user=self.request.user, cart=cart, total_price=total_price)

        try:
            response = initiate_payment(total_price, order.id)
        except Exception as e:
            order.delete()
            return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse(response)
