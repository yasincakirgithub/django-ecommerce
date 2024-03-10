from django.contrib import admin
from blog.models import Blog,Tags,Category,Comment
# Register your models here.

admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)