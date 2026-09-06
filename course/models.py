from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Course(models.Model):

    class Level(models.TextChoices):
        BEGINNER = 'beginner' , 'Beginner'
        INTERMIDIATE = 'intermidiate','Intermidiate'
        ADVANCED = 'advanced','Advanced'

    class Status(models.TextChoices):
        DRAFT = 'draft','Draft'
        PUBLISHED = 'published','Published'

    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='courses_created'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='courses-thumbnail/')
    level = models.CharField(max_length=20,choices=Level,default=Level.INTERMIDIATE)
    status = models.CharField(max_length=20,choices=Status,default=Status.DRAFT)
    price = models.IntegerField(null=True,blank=True)
    category = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class CourseVideo(models.Model):

    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='videos')
    title = models.CharField(max_length=255)
    video_files = models.FileField(upload_to='course-videos/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class Enrollment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user','course']

class InVoice(models.Model):

    class Status(models.TextChoices):
        PENDING = 'pending','Pending'
        PAID = 'paid' ,'Paid'
        FAILED = 'failed','Failed'

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(blank=True,null=True)
    payment_reference  = models.CharField(max_length=300,blank=True,null=True)

    class Meta:
        ordering = ['-created_at']

    def mark_paid(self,reference_code):
        self.status = self.Status.PAID
        self.paid_at = timezone.now()
        self.payment_reference = reference_code
        self.save()