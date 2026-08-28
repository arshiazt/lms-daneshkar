from django.shortcuts import render,get_object_or_404
from .models import Profile
from django.views.generic import ListView,DetailView

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