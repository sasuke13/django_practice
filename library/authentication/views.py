from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CustomUser


def auth_register_user(request):
    if request.method == "POST":
        usr = CustomUser()
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        middle_name = request.POST["middle_name"]
        last_name = request.POST["last_name"]
        role = request.POST["role"]
        if usr.get_by_email(email=email):
            messages.success(request, "User with such am email already exists")
            return render(request, "authentication/register_user.html")
        if int(role) == 1:
            CustomUser.objects.create_superuser(email=email, password=password, first_name=first_name,
                                                    middle_name=middle_name, last_name=last_name, is_active=True)
        else:
            CustomUser.objects.create_user(email=email, password=password, first_name=first_name,
                                                    middle_name=middle_name, last_name=last_name, is_active=True)

        messages.success(request, "User was successfully created!")
        return redirect('login')
    else:
        return render(request, "authentication/register_user.html")

    # else:
    #     return render(request, "authentication/register_user.html")


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]
        usr = CustomUser.objects.filter(email=email, role=role).first()
        user = authenticate(request, email=email, password=password, role=role)
        if usr:
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request, "Wrong password, email or chosen role. Try again")
                return redirect('login')
        else:
            messages.success(request, "Wrong password, email or chosen role. Try again")
            return redirect('login')

    else:
        return render(request, "authentication/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('login')
