from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):

    def _create_user(self,phone,password=None,**extra_fields):

        first_name = extra_fields.get('first_name')
        last_name = extra_fields.get('last_name')
        if not phone:
            raise ValueError('The phone field must be set.')
        if not first_name or not last_name:
            raise ValueError('The fullname field must be set.')
        user=self.model(phone=phone,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user 
    
    def create_user(self,phone,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        return self._create_user(phone,password,**extra_fields)
    
    def create_superuser(self,phone,password=None,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(phone,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):

    phone=models.CharField(max_length=11,unique=True,verbose_name='شماره تلفن')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects=UserManager()
    
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=['first_name','last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'