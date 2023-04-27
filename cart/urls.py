from django.urls import path

from .views import CartView, CartItemView, CartItemDetailView

urlpatterns = [
    path('<int:pk>/', CartView.as_view()),
    path('items/', CartItemView.as_view()),
    path('item/<int:pk>/', CartItemDetailView.as_view())
]
