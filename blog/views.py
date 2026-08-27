from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_view(request):
    context = {
        'name':'arshiazt',
        'skills':['python','django','drf']
    }
    return render(request,'home.html',context)

def test_id(request,pid):
    return HttpResponse(f'Pid : {pid}')