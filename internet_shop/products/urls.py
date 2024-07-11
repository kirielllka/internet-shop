from django.urls import path, include


from .roater import router as router

urlpatterns = [
    path('', include(router.urls)),
]