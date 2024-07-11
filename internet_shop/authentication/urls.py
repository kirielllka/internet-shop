from django.urls import path, include

from .views import RegisterView, LoginView, LogoutView, UserPasswordUpdate, UserAPIVIEW, UserDelete
from .router import router as authenticate_router

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('changepassword/<int:id>', UserPasswordUpdate.as_view(), name='change_password'),
    path('users/', UserAPIVIEW.as_view(), name='userapi')
    path('users/<int:id>', UserAPIVIEW.as_view(), name='userapi-retrieve'),
    path('users_delete/<int:id>', UserDelete.as_view(), name='userapi-delete'),
    path('', include(authenticate_router.urls)),
]