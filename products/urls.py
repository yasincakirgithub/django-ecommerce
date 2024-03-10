from django.urls import path
from products.views import (ProductDetailPage,ProductListPage)
urlpatterns = [
    path('',ProductListPage,name='product-page'),
    path('<str:slug>/',ProductDetailPage,name='product-detail-page')
]
    
