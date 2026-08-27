from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    full_name = models.CharField(max_length=128)
    class Role(models.TextChoices):
        STUDENT = 'student', _('Student')
        INSTRUCTOR = 'instrauctor', _('Instrauctor')
        STAFF = 'staff', _('Staff')
    role = models.CharField(max_length=20,choices=Role.choices,default=Role.STUDENT)
    avatar = models.ImageField(upload_to='profile-avatar/',blank=True,null=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    course_enrolled = models.PositiveIntegerField(default=0,editable=False)
    course_completed = models.PositiveIntegerField(default=0,editable=False)
    rating = models.DecimalField(max_digits=3,decimal_places=2,blank=True,null=True,editable=False)
    github_link = models.URLField(blank=True,null=True)
    linkedin_link = models.URLField(blank=True,null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name