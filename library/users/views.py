from django.shortcuts import render, redirect
from authentication.models import CustomUser
from django.contrib import messages


def main_page(request):
    return render(request, "users/users.html")


def get_certain_user(request):
    if request.method == "POST":
        usr = CustomUser()
        email = request.POST["email"]
        usr = usr.get_by_email(email)
        if usr:
            return render(request, "users/users.html", {"text": usr})
        else:
            messages.success(request, "There is no such an user")
            return render(request, "users/users.html")
    return render(request, "users/users.html")


def get_all_users(request):
    return render(request, "users/users.html", {"text": CustomUser.get_all()})
