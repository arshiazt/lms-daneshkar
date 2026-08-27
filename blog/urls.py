from django.urls import path
from .views import my_view

urlpatterns = [
    path('home/', my_view,name='home'),
]