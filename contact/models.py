from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)
    message = models.TextField()