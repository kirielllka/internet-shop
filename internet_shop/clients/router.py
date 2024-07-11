from rest_framework import routers

from clients import views


router = routers.DefaultRouter()

router.register(r'clients', views.ClientViewSet, basename="clients")

