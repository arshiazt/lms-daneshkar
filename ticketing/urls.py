from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tickets',TicketViewSet,basename='ticket')
router.register('message',TicketMessageViewSet,basename='message')

urlpatterns = [
    path('',include(router.urls)),
]