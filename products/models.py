from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
# Create your models here.

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product')

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class ProductSize(models.Model):
    name = models.CharField(choices=(('xxl','xxl'),('xl','xl'),('l','l'),('m','m'),('s','s'),('xs','xs')),max_length=50)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    currency = models.CharField(choices=[('$','USD'),('€','EUR')],max_length=5)
    description = models.TextField(null=True,blank=True)
    additional_information = models.TextField(null=True,blank=True)
    code = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory,models.SET_NULL,null=True)
    images = models.ManyToManyField(ProductImage,blank=True)
    
    slug = AutoSlugField(populate_from='name',unique_with=['id', 'created_at'], editable=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    @property
    def is_new(self):
        return  self.created_at >  timezone.now() - timezone.timedelta(hours=5) 

    def __str__(self) -> str:
        return self.name

class ProductStock(models.Model):
    product = models.ForeignKey(Product,models.CASCADE,related_name="stocks")
    size = models.ForeignKey(ProductSize,models.CASCADE)
    amount = models.IntegerField(default=0)