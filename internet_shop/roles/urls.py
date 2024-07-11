from django.urls import path, include

from .roater import router as client_router

urlpatterns = [
    path('', include(client_router.urls)),
]
