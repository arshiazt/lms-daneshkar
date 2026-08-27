from django.urls import path
from .views import my_view,test_id,contact_view

urlpatterns = [
    path('portfolio/', contact_view,name='portfolio'),
]