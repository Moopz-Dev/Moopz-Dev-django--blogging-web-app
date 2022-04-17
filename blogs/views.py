from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.


def index(request):
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    latest = Blog.objects.all().order_by('-pk')[:4]

    # Popular posts
    popular = Blog.objects.all().order_by('-views')[:3]

    # Recommended posts
    suggestion = Blog.objects.all().order_by('views')[:3]

    # pagination
    paginator = Paginator(blogs, 3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        blogPerPage = paginator.page(page)
    except(EmptyPage, InvalidPage):
        blogPerPage = paginator.page(paginator.num_pages)
    return render(request, "frontend/index.html", {'categories': categories, "blogs": blogPerPage, "latest": latest, "popular": popular, "suggestion": suggestion})


def blogDetail(request, id):
    categories = Category.objects.all()
    popular = Blog.objects.all().order_by('-views')[:3]
    suggestion = Blog.objects.all().order_by('views')[:3]

    singleBlog = Blog.objects.get(id=id)
    singleBlog.views = singleBlog.views + 1
    singleBlog.save()
    return render(request, "frontend/blogDetail.html", {"blog": singleBlog, "categories": categories, "popular": popular, "suggestion": suggestion})


def searchCategory(request, category_id):
    categoryName = Category.objects.get(id=category_id)
    categories = Category.objects.all()
    blogs = Blog.objects.filter(category_id=category_id)
    popular = Blog.objects.all().order_by('-views')[:3]
    suggestion = Blog.objects.all().order_by('views')[:3]
    return render(request, "frontend/searchCategory.html", {"blogs": blogs, "categories": categories, "popular": popular, "suggestion": suggestion, "categoryName": categoryName})


def searchWriter(request, writer):
    categories = Category.objects.all()
    blogs = Blog.objects.filter(writer=writer)
    popular = Blog.objects.all().order_by('-views')[:3]
    suggestion = Blog.objects.all().order_by('views')[:3]
    return render(request, "frontend/searchWriter.html", {"writerName": writer, "categories": categories, "blogs": blogs, "popular": popular, "suggestion": suggestion})
