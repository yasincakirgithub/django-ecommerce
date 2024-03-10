from django.shortcuts import render,redirect
from django.urls import reverse
from django.db.models import Count,Prefetch
from blog.models import Blog,Comment
from blog.forms import CommentForm
from django.contrib import messages
# Create your views here.

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

def BlogPage(request):

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    
    filter_criteria = {}
    filtered_title = request.GET.get('blog-title',None)
    filtered_tag = request.GET.get('blog-tag',None)
    filtered_category = request.GET.get('blog-category',None)
    if filtered_title:
        filter_criteria["title__icontains"] = filtered_title
    if filtered_tag:
        filter_criteria["tags__id"] = filtered_tag
    if filtered_category:
        filter_criteria["category__id"] = filtered_category

    blogs = Blog.objects.select_related("created_by","category").prefetch_related( Prefetch('comments', queryset=Comment.objects.select_related('user'))).filter(**filter_criteria).order_by("-created_at")

    paginator = Paginator(blogs,per_page=4, request=request)
    page_obj = paginator.page(page)

    # Popular items
    popular_tags = Blog.objects.values('tags__name','tags__id').annotate(tag_count=Count('tags__id')).order_by('-tag_count')[0:5]
    popular_categories = Blog.objects.values('category__name','category__id').annotate(category_count=Count('category__id')).order_by('-category_count')[0:5]

    return render(
        request,
        'blog/index.html',
        context={
            'page_obj': page_obj,
            'popular_tags':popular_tags,
            'popular_categories':popular_categories
        })

def BlogDetailPage(request,slug):

    # blog = Blog.objects.prefetch_related('comments__user').get(slug=slug)
    blog = Blog.objects.select_related("created_by","category").prefetch_related( Prefetch('comments', queryset=Comment.objects.select_related('user'))).get(slug=slug)
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            messages.success(request, 'Your comment added')
            return redirect(reverse("blog-detail-page",kwargs={"slug":blog.slug}))   
    else:
        comment_form = CommentForm()
    # Popular items
    popular_tags = Blog.objects.values('tags__name','tags__id').annotate(tag_count=Count('tags__id')).order_by('-tag_count')[0:5]
    popular_categories = Blog.objects.values('category__name','category__id').annotate(category_count=Count('category__id')).order_by('-category_count')[0:5]

    return render(
        request,
        'blog/detail.html',
        context={
            'blog': blog,
            'comment_form':comment_form,
            'popular_tags':popular_tags,
            'popular_categories':popular_categories
        })