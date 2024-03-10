from django.db import models
from users.models import CustomUserModel
from autoslug import AutoSlugField
# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    tags = models.ManyToManyField(Tags, blank=True)
    image = models.ImageField(upload_to='blog')

    category = models.ForeignKey(Category,models.SET_NULL,null=True)
    created_by = models.ForeignKey(CustomUserModel,models.CASCADE)

    slug = AutoSlugField(populate_from='title',unique_with=['id', 'created_at'])

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

class Comment(models.Model):

    blog = models.ForeignKey(Blog,models.CASCADE, related_name="comments")
    user = models.ForeignKey(CustomUserModel,models.CASCADE)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)