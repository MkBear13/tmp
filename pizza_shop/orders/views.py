from django.shortcuts import render

from rest_framework import viewsets
from .models import Product, Order, User, Buyer, Admin
from .serializers import ProductSerializer, OrderSerializer, UserSerializer, BuyerSerializer, AdminSerializer
from .utils import send_order_ready_email

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.status == 'completed':
            send_order_ready_email(instance)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer