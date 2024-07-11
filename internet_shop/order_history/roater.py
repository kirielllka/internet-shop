from rest_framework import routers
from .views import OrderListViewSet
router = routers.DefaultRouter()

router.register(r'product', OrderListViewSet, basename="product")