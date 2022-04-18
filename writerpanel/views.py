from django.shortcuts import render
from blogs.models import Blog
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from category.models import Category
# Create your views here.


@login_required(login_url="member")
def panel(request):
    writer = auth.get_user(request)
    blogs = Blog.objects.filter(writer=writer)
    blogCount = blogs.count()
    total = blogs.aggregate(Sum("views"))
    return render(request, "backend/index.html", {"blogs": blogs, "writer": writer, "blogCount": blogCount, "total": total})


def displayForm(request):
    writer = auth.get_user(request)
    blogs = Blog.objects.filter(writer=writer)
    blogCount = blogs.count()
    total = blogs.aggregate(Sum("views"))
    categories = Category.objects.all()
    return render(request, 'backend/blogForm.html', {"blogs": blogs, "writer": writer, "blogCount": blogCount, "total": total, 'categories': categories})
