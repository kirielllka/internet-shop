from django.urls import path, include

from .router import router as client_router

urlpatterns = [
    path('', include(client_router.urls)),
]
