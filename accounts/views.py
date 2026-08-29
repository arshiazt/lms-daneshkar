from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def user_register_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,f'{user.first_name} create')
            return redirect('portfolio')
        else:
            messages.error(request,'cant create this user')
    form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

def user_login_view(request):

    if request.method == 'POST':
        form = UserLoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,f'{user.first_name} login')
            return redirect('portfolio')
        else:
            messages.error(request,'Username or Password is incorrect')
    form = UserLoginForm()
    return render(request,'login.html',{'form':form})

def user_logout_view(request):
    logout(request)
    messages.success(request,'user logout')
    return redirect('portfolio')