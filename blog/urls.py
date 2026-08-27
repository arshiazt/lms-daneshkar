from django.urls import path
from .views import my_view,test_id

urlpatterns = [
    path('home/', my_view,name='home'),
    path('test-pid/<int:pid>',test_id,name='test-id'),
]