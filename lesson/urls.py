from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lessons',LessonViewSet,basename='lessons')
router.register(r'contents',LessonContentViewSet,basename='contents')

urlpatterns = [
    path('',include(router.urls))
]