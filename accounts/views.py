from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def user_register_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('portfolio')
    form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

def user_login_view(request):

    if request.method == 'POST':
        form = UserLoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('portfolio')
    form = UserLoginForm()
    return render(request,'login.html',{'form':form})

def user_logout_view(request):
    logout(request)
    return redirect('portfolio')