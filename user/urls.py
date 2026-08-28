from django.urls import path
from .views import *

urlpatterns = [
    # path('profiles/',profiles_list_view,name="profiles-list"),
    # path('profiles/<int:pk>',profile_detail,name="profile-detail"),
    path('profiles/',ProfilesListView.as_view(),name="profiles-list"),
    path('profiles/<int:pk>',ProfileDetailView.as_view(),name="profile-detail"),
]
