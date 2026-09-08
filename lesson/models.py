from django.db import models
from django.contrib.auth import get_user_model
from course.models import *
# Create your models here.

User = get_user_model()

class Lesson(models.Model):

    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    class Meta:
        unique_together = ('course','order')
        ordering = ['order']

    def __str__(self):
        return f'{self.course.title} - {self.title}'
    
class LessonContent(models.Model):

    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='contents')
    video_url = models.URLField(blank=True,null=True)
    pdf_file = models.FileField(upload_to='lesson-pdf/',blank=True,null=True)
    extra_links = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'Content for {self.lesson.title}'