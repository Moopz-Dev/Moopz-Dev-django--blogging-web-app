from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
# Create your views here.


def index(request):
    categories = Category.objects.all()
    return render(request, "frontend/index.html", {'categories': categories})
