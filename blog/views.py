from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
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

class BookListApiView(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']
    search_fields = ['title']
    ordering_fields = ['title']