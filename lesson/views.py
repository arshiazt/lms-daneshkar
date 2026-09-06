from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import viewsets

# Create your views here.

class LessonViewSet(viewsets.ModelViewSet):

    queryset  = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [IsAdminOrInstructor()]
        return [IsStudentOrReadOnly()]
    
class LessonContentViewSet(viewsets.ModelViewSet):

    queryset  = LessonContent.objects.all()
    serializer_class = LessonContentSerializer

    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [IsAdminOrInstructor()]
        return [IsStudentOrReadOnly()]