from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.


def user_register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"{user.first_name} create")
            return redirect("portfolio")
        else:
            messages.error(request, "cant create this user")
    form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


def user_login_view(request):

    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"{user.first_name} login")
            return redirect("portfolio")
        else:
            messages.error(request, "Username or Password is incorrect")
    form = UserLoginForm()
    return render(request, "login.html", {"form": form})


def user_logout_view(request):
    logout(request)
    messages.success(request, "user logout")
    return redirect("portfolio")


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("portfolio")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, f"{self.object.first_name} create")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "cant create this user")
        return super().form_invalid(form)


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "login.html"
    next_page = reverse_lazy("portfolio")

    def form_valid(self, form):
        messages.success(self.request, f"{self.request.user.username} login")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Username or Password is incorrect")
        return super().form_invalid(form)


class UserLogoutView(LogoutView):

    next_page = reverse_lazy("portfolio")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "user logout")
        return super().dispatch(request, *args, **kwargs)


# Api view

from django.contrib.auth import login, logout
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *


class RegisterApiView(generics.CreateAPIView):

    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)
        return user


class CustomLoginApiView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LogoutApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            logout(request)
            return Response({"detail": "User logout successfully"}, status=200)
        except Exception:
            return Response({"detail": "token is wrong"}, status=400)
