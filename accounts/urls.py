from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    # path('register/',UserRegisterView.as_view(),name='register'),
    # path('login/',UserLoginView.as_view(),name='login'),
    # path('logout/',UserLogoutView.as_view(),name='logout'),
    path("api/auth/register/", RegisterApiView.as_view(), name="register-api"),
    path("api/auth/login/", CustomLoginApiView.as_view(), name="login-api"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="refresh-api"),
    path("api/auth/logout/", LogoutApiView.as_view(), name="logout-api"),
]
