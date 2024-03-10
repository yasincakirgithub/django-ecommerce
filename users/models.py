from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager

# Create your models here.

class CustomUserModel(AbstractUser):
    
    username = None
    date_joined = None

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    profile_img = models.ImageField(null=True,upload_to='profile-img')

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
