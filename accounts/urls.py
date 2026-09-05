from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

urlpatterns = [
    path("api/auth/register/", RegisterApiView.as_view(), name="register-api"),
    path("api/auth/login/", CustomLoginApiView.as_view(), name="login-api"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="refresh-api"),
    path("api/auth/logout/", LogoutApiView.as_view(), name="logout-api"),
    path("api/auth/password-reset/request/", RequestPasswordResetView.as_view(), name="request-password-reset"),
    path("api/auth/password-reset/verify/", VerifyOTPAndResetPasswordView.as_view(), name="verify-otp-reset-password"),
]
