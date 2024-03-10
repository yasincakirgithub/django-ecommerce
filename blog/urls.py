from django.urls import path
from blog.views import (BlogPage,BlogDetailPage)
urlpatterns = [
    path('',BlogPage,name='blog-page'),
    path('<str:slug>/',BlogDetailPage,name='blog-detail-page')

]
    
