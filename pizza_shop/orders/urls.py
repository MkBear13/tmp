from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, UserViewSet, BuyerViewSet, AdminViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'users', UserViewSet)
router.register(r'buyers', BuyerViewSet)
router.register(r'admins', AdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
