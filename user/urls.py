from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles',ProfileViewSet,basename='profiles-viewset')

urlpatterns = [
    # path('profiles/',profiles_list_view,name="profiles-list"),
    # path('profiles/<int:pk>',profile_detail,name="profile-detail"),
    # path('profiles/',ProfilesListView.as_view(),name="profiles-list"),
    # path('profiles/<int:pk>',ProfileDetailView.as_view(),name="profile-detail"),
    # path('subscribe/',subscibe,name="subscribe"),
    path('fbv/profiles/',profile_list_api_view,name='fbv-profiles'),
    path('cbv/profiles/',ProfileListApiView.as_view(),name='cbv-profiles'),
    path('generics/profiles/',ProfileListCreateApiView.as_view(),name='generics-profiles-list'),
    path('generics/profiles/<int:pk>/',ProfileRetrieveUpdateDestroyAPIView.as_view(),name='generics-profile-detail'),
    path('viewset/',include(router.urls))
]
