from django.db import models

# Create your models here.

class SocialMedia(models.Model):
    platform = models.CharField(max_length=50)
    url =  models.CharField(max_length=150)

    def __str__(self) -> str:


        return self.platform
