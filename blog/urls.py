from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'book',BookViewSet,basename='book')

urlpatterns = [
    # path("portfolio/", contact_view, name="portfolio"),
    # path('test/',test_view,name='test'),
    path('api/books/',BookListApiView.as_view(),name='bookss-list'),
    path('viewset/',include(router.urls)),
]
