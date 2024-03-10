from django.db import models

# Create your models here.

class About(models.Model):
    image = models.ImageField(upload_to='about-image')
    title = models.CharField(max_length=50)
    content = models.TextField()

class DailyMessage(models.Model):
    content = models.TextField()
    message_owner = models.CharField(max_length=100)