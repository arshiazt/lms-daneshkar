from django.shortcuts import render

# Create your views here.

def my_view(request):
    context = {
        'name':'arshiazt',
        'skills':['python','django','drf']
    }
    return render(request,'home.html',context)