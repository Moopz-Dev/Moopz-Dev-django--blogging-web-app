from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'backend/login_register.html')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if username == "" or email == "" or password == "" or repassword == "":
            messages.info(request, "Please enter data into all fields.")
            return redirect("member")
        else:
            if password == repassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "This username already exist.")
                    return redirect("member")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "This email already exist.")
                    return redirect("member")
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    messages.info(request, "Account created.")
                    return redirect("member")
            else:
                messages.info(request, "Passwords do not match.")
                return redirect("member")
