from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):

    def _create_user(self,phone,password=None,**extra_fields):
        if not phone:
            raise ValueError('The phone field must be set.')
        user=self.model(phone=phone,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user 
    
    def create_user(self,phone,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        return self._crete_user(phone,password,**extra_fields)
    
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
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object=UserManager()
    
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.phone