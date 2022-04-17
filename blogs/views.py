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
    return render(request, "frontend/index.html", {'categories': categories, "blogs": blogPerPage, "latest": latest})
