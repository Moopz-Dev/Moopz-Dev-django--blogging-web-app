from django.shortcuts import redirect, render
from blogs.models import Blog
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from category.models import Category
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.


@login_required(login_url="member")
def panel(request):
    writer = auth.get_user(request)
    blogs = Blog.objects.filter(writer=writer)
    blogCount = blogs.count()
    total = blogs.aggregate(Sum("views"))
    return render(request, "backend/index.html", {"blogs": blogs, "writer": writer, "blogCount": blogCount, "total": total})


@login_required(login_url="member")
def displayForm(request):
    writer = auth.get_user(request)
    blogs = Blog.objects.filter(writer=writer)
    blogCount = blogs.count()
    total = blogs.aggregate(Sum("views"))
    categories = Category.objects.all()
    return render(request, 'backend/blogForm.html', {"blogs": blogs, "writer": writer, "blogCount": blogCount, "total": total, 'categories': categories})


@login_required(login_url="member")
def insertData(request):
    if request.method == "POST" and request.FILES["image"]:
        datafile = request.FILES["image"]
        name = request.POST["name"]
        category = request.POST["category"]
        description = request.POST["description"]
        content = request.POST["content"]
        writer = auth.get_user(request)

        if str(datafile.content_type).startswith("image"):
            fs = FileSystemStorage()
            img_url = "blogImages/"+datafile.name
            filename = fs.save(img_url, datafile)
            blog = Blog(name=name, description=description,
                        category_id=category, content=content, writer=writer, image=img_url)
            blog.save()
            messages.info(request, "Data Successfully Written!")
            return redirect("panel")
        else:
            messages.info(request, "Invalid file type, please reupload!")
            return redirect("displayForm")


@login_required(login_url="member")
def deleteData(request, id):
    try:
        blog = Blog.objects.get(id=id)
        fs = FileSystemStorage()
        fs.delete(str(blog.image))
        blog.delete()
        return redirect('panel')
    except:
        return redirect('panel')


@login_required(login_url="member")
def editData(request, id):
    blogEdit = Blog.objects.get(id=id)
    writer = auth.get_user(request)
    blogs = Blog.objects.filter(writer=writer)
    blogCount = blogs.count()
    total = blogs.aggregate(Sum("views"))
    categories = Category.objects.all()
    return render(request, "backend/editForm.html", {"blogEdit": blogEdit, "writer": writer, "blogCount": blogCount, "total": total, 'categories': categories})


@login_required(login_url="member")
def updateData(request, id):
    try:
        if request.method == "POST":
            blog = Blog.objects.get(id=id)
            name = request.POST["name"]
            category = request.POST["category"]
            description = request.POST["description"]
            content = request.POST["content"]

            blog.name = name
            blog.category_id = category
            blog.description = description
            blog.content = content
            blog.save()
            messages.info(request, "Data Successfully Updated!")

            if request.FILES["image"]:
                datafile = request.FILES["image"]
                if str(datafile.content_type).startswith("image"):
                    fs = FileSystemStorage()
                    fs.delete(str.blog.image)
                    img_url = "blogImages/"+datafile.name
                    filename = fs.save(img_url, datafile)
                    blog.image = img_url
                    blog.save()
                return redirect("panel")
            return redirect("panel")

    except:
        return redirect("panel")
