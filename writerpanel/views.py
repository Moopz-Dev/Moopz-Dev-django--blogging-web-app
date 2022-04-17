from django.shortcuts import render
from blogs.models import Blog
from django.db.models import Sum
# Create your views here.


def panel(request):
    writer = "moopz"
    blogs = Blog.objects.filter(writer=writer)
    blogCount = blogs.count()
    total = blogs.aggregate(Sum("views"))
    return render(request, "backend/index.html", {"blogs": blogs, "writer": writer, "blogCount": blogCount, "total": total})
