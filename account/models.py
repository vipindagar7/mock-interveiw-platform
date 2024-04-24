from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
class Custom_user(AbstractUser):
    username = None
    email = models.EmailField(max_length=254 , unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100 , blank=True , null = True)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_interviewer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return f"user is {self.email} with id {str(self.id)}"
    
    
    
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(Custom_user , on_delete=models.CASCADE, unique=True)
    field = models.CharField(max_length=100 , blank=True , null = True)
    gender = models.CharField(max_length=100 , blank=True , null = True)
    mobile = models.IntegerField(blank=True , null = True)
    skills = models.TextField(blank=True, null = True)
    intrests = models.TextField(blank=True, null = True)
    location = models.CharField(max_length=100 , blank=True)
    twitter = models.CharField(max_length=100 , blank=True, null = True)
    github = models.CharField(max_length=100 , blank=True , null = True)
    linkedin = models.CharField(max_length=100 , blank=True , null = True)
    instagram = models.CharField(max_length=100 , blank=True , null = True)
    bio = models.TextField(max_length=500 , blank=True , null = True)
    image = models.ImageField(upload_to='media/' , blank=True , null = True)
    referal_code = models.CharField(max_length=100 , blank=True , null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    is_public = models.BooleanField(default=False)
    def __str__(self):
        return f"profile of {self.user.email}" 
        
class InterviewerProfile(models.Model): 
    user = models.OneToOneField(Custom_user , on_delete=models.CASCADE, unique=True)
    field = models.CharField(max_length=100 , blank=True , null = True)
    gender = models.CharField(max_length=100 , blank=True , null = True)
    mobile = models.IntegerField(blank=True , null = True)
    company = models.CharField(max_length=100 , blank=True , null = True)
    position = models.CharField(max_length=100 , blank=True , null = True)
    experience = models.CharField(max_length=100 , blank=True , null = True)
    skills = models.TextField(blank=True, null = True)
    intrests = models.TextField(blank=True, null = True)
    location = models.CharField(max_length=100 , blank=True)
    twitter = models.CharField(max_length=100 , blank=True, null = True)
    github = models.CharField(max_length=100 , blank=True , null = True)
    linkedin = models.CharField(max_length=100 , blank=True , null = True)
    instagram = models.CharField(max_length=100 , blank=True , null = True)
    bio = models.TextField(max_length=500 , blank=True , null = True)
    image = models.ImageField(upload_to='media/' , blank=True , null = True)
    referal_code = models.CharField(max_length=100 , blank=True , null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"profile of interviewer {self.user}"