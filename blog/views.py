from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_view(request):
    context = {"name": "arshiazt", "skills": ["python", "django", "drf"]}
    return render(request, "portfolio.html", context)


def test_id(request, pid):
    return HttpResponse(f"Pid : {pid}")


def contact_view(request):

    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"{name} ---> {message}")
    return render(request, "portfolio.html")

def test_view(request):

    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"{name} {message}")
    return render(request, "test.html")