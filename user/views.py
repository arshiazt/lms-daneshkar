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

class ProfileListApiView(APIView):

    def get(self,request):

        profile = Profile.objects.all()
        serializer_class = ProfileSerializer(profile,many=True)
        return Response(serializer_class.data)
    
class ProfileListCreateApiView(ListCreateAPIView):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileViewSet(ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer