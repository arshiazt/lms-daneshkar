from django.urls import path

from .views import contact_view, my_view, test_id

urlpatterns = [
    path("portfolio/", contact_view, name="portfolio"),
]
