from django.urls import path

from .views import contact_view, my_view, test_id,test_view

urlpatterns = [
    path("portfolio/", contact_view, name="portfolio"),
    path('test/',test_view,name='test'),
]
