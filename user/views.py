from django.shortcuts import render,get_object_or_404
from .models import Profile
from django.views.generic import ListView,DetailView
from .forms import UserForms
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.throttling import *
from .throttles import *
import django_filters.rest_framework as filters
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

# Create your views here.

def profiles_list_view(request):
    profiles = Profile.objects.select_related('user')
    return render(request,'profile-list.html',{'profiles':profiles})

def profile_detail(request,pk):
    profile = get_object_or_404(Profile,pk=pk)
    return render(request,'profile-detail.html',{'profile':profile})

class ProfilesListView(ListView):
    model = Profile
    queryset = Profile.objects.select_related('user')
    # queryset = Profile.objects.filter(role__exact='Student')
    # queryset = Profile.objects.filter(role__iexact='Student')
    # queryset = Profile.objects.filter(role__contains='st')
    # queryset = Profile.objects.filter(role__iexact='STudent')
    template_name = 'profile-list.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile-detail.html'
    context_object_name = 'profile'

def subscibe(request):

    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            return HttpResponse(f'email send : {email}')
    form = UserForms()
    return render(request,'subscribe.html',{'form':form})

@api_view(['GET'])
def profile_list_api_view(request):

    profile = Profile.objects.all()
    serializer_class = ProfileSerializer(profile,many=True)
    return Response(serializer_class.data)

# class ProfileListApiView(APIView):
#     throttle_classes = [UserRateThrottle]
#     def get(self,request):

#         profile = Profile.objects.all()
#         serializer_class = ProfileSerializer(profile,many=True)
#         return Response(serializer_class.data)

class ProfileFilter(filters.FilterSet):

    course_enrolled_min = filters.NumberFilter(field_name='course_enrolled',lookup_expr='gte')
    course_enrolled_max = filters.NumberFilter(field_name='course_enrolled',lookup_expr='lte')
    rating_min = filters.NumberFilter(field_name='rating_min',lookup_expr='gte')
    rating_max = filters.NumberFilter(field_name='rating_max',lookup_expr='lte')

    class Meta:
        model = Profile
        fields = ['role','location']

class ProfilePagination(PageNumberPagination):

    page_size = 4
    page_query_param = 'page'
    max_page_size = 10

@method_decorator(cache_page(60 * 5),name='dispatch')
class ProfileListApiView(ReadOnlyModelViewSet):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProfileFilter
    search_fields = ['full_name',]
    ordering_fields = ['created_at','rating','full_name']
    ordering = ['-created_at']
    pagination_class = ProfilePagination

class ProfileListCreateApiView(ListCreateAPIView):
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'profile'
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileViewSet(ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CachedView(APIView):

    def get(self,request):
        data = cache.get('profile_stats')
        if not data:
            total = Profile.objects.count()
            top_rating = Profile.objects.order_by('-rating').first()
            data = {
                'count':total,
                'top_user':top_rating.full_name if top_rating else None
            }
            cache.set('profile_stats',data,timeout=300)
        return  Response(data)
    
@receiver(post_save,sender=Profile)
def clear_profile_cache(sender,instance,**kwargs):
    cache.delete('profile_stats')
    cache.delete_pattern('views.decorators.cache*')