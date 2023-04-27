from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Item
from .serializers import ItemSerializer
# Create your views here.


class ItemListView(ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
