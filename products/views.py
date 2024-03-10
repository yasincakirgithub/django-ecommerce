from django.shortcuts import render,redirect
from django.urls import reverse
from django.db.models import Count,Prefetch
from products.models import Product
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def ProductDetailPage(request,slug):

    product = Product.objects.select_related("category").prefetch_related("stocks").get(slug=slug)
    
    return render(
        request,
        'products/detail.html',
        context={
            'product': product
        })



def ProductListPage(request):

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    filter_criteria = {}
    filtered_name = request.GET.get('product-name',None)
    filtered_category = request.GET.get('product-category',None)
    if filtered_name:
        filter_criteria["name__icontains"] = filtered_name
    if filtered_category:
        filter_criteria["category__id"] = filtered_category

    products = Product.objects.filter(**filter_criteria).select_related("category")
    
    paginator = Paginator(products,per_page=20, request=request)
    page_obj = paginator.page(page)

    popular_categories = Product.objects.values('category__name','category__id').annotate(category_count=Count('category__id')).order_by('-category_count')[0:5]
    
    return render(
        request,
        'products/list.html',
        context={
            'page_obj': page_obj,
            'popular_categories':popular_categories
        })