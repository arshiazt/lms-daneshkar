from django.shortcuts import render,get_object_or_404
from .models import Profile

# Create your views here.

def profiles_list_view(request):
    profiles = Profile.objects.select_related('user')
    return render(request,'profile-list.html',{'profiles':profiles})

def profile_detail(request,pk):
    profile = get_object_or_404(Profile,pk=pk)
    return render(request,'profile-detail.html',{'profile':profile})