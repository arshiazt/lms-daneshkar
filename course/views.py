from django.core.cache import cache
from django.db.models import Count
from rest_framework import viewsets,permissions,generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from django_redis import get_redis_connection
from .models import *
from .serializers import *
from.permissions import *
from rest_framework.views import  APIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from notification.tasks import *

class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all().select_related('instructor').prefetch_related('videos').order_by('-created_at')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['level','category','status','price']
    search_fields = ['title','description']
    ordering_fields = ['created_at','price','title']

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [IsInstructorOrAdmin]
        return super().get_permissions()

class UserEnrolledCourseView(generics.ListAPIView):

    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user).select_related('course')
    
class RecommendedCourseView(generics.ListAPIView):

    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        key = f'recommended_{self.request.user.id}'
        cached_data = cache.get(key)
        if cached_data:
            return cached_data
        courses = Course.objects.annotate(
            num_students=Count('enrollment')
        ).filter(status='published').order_by('-num_students')[:5]
        cache.set(key,courses,60*10)
        return courses
    
class CreateInVoiceView(generics.CreateAPIView):

    queryset  = InVoice.objects.all()
    serializer_class = InVoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        course_id = self.request.data.get('course')
        course = get_object_or_404(Course,id=course_id,status=Course.Status.PUBLISHED)
        existing_invoice = InVoice.objects.filter(user=self.request.user,course=course,status=InVoice.Status.PENDING).first()

        if existing_invoice:
            serializer.instance = existing_invoice
        else:
            serializer.save(user=self.request.user,course=course,amount=course.price)
            send_notification_task.delay(
                user_id=self.request.user.id,
                title='create new invoice',
                message=f'{course.title} invoice'
            )

class PayInvoiceView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,invoice_id):
        invoice = get_object_or_404(InVoice,id=invoice_id,user=self.request.user,status=InVoice.Status.PENDING)
        # bank api connection
        fake_reference_code = f'11:25:34.10:02:1405'
        invoice.mark_paid(fake_reference_code)

        Enrollment.objects.get_or_create(user=request.user,course=invoice.course)
        send_notification_task.delay(
                user_id=self.request.user.id,
                title='successful payment',
                message=f'payment for {invoice.id} course was successful'
            )
        return Response({'detail':'Pay done...','payment_reference':fake_reference_code})