from django.contrib import admin
from products.models import Product,ProductCategory,ProductImage,ProductSize,ProductStock
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields if not isinstance(field, (ManyToOneRel, ForeignKey, OneToOneField,))]
admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields if not isinstance(field, (ManyToOneRel,OneToOneField,))]
admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields if not isinstance(field, (ManyToOneRel,  OneToOneField,))]
admin.site.register(ProductImage, ProductImageAdmin)

class ProductSizeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductSize._meta.fields if not isinstance(field, (ManyToOneRel,  OneToOneField,))]
admin.site.register(ProductSize, ProductSizeAdmin)

class ProductStockAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductStock._meta.fields if not isinstance(field, (ManyToOneRel, OneToOneField,))]
admin.site.register(ProductStock, ProductStockAdmin)
