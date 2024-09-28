from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def user_logout(request):
    logout(request)
    return redirect("login")


def user_profile(request):
    return render(request, "user/profile.html")


def user_login(request):
    msg = ""
    user = None
    username = request.session.get("username", "")
    if request.method == "POST":
        if request.POST.get("register"):
            return redirect("register")

        if request.POST.get("login"):
            username = request.POST.get("username")
            password = request.POST.get("password")

            if username == "" or password == "":
                msg = "帳號密碼不能為空!"
            else:
                user = authenticate(request, username=username, password=password)

                if user:
                    msg = "登入成功!"
                    login(request, user)
                    return redirect("profile")
                else:
                    msg = "帳號或密碼錯誤!"

    return render(
        request, "user/login.html", {"msg": msg, "user": user, "username": username}
    )


def user_register(request):
    msg = ""

    # if request.method == "GET":
    form = UserCreationForm()

    # all,get,filter
    # print(User.objects.all())
    # print(User.objects.get(username="tjtyjty"))
    # print(User.objects.filter(username="tjtyjty"))

    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 比對密碼長度8,比對密碼是否相同
        if len(password1) != 8 or len(password2) != 8:
            msg = "密碼長度不正確"

        elif password1 != password2:
            msg = "兩次密碼不一樣"

        else:
            # 比對使用者是否存在
            if User.objects.filter(username=username):
                msg = "帳號已存在!"

            # 註冊使用者
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                msg = "註冊成功!"
                request.session["username"] = user.username
                return redirect("login")
                # return render(request, "user/login.html", {"user": user})

    return render(request, "user/register.html", {"form": form, "msg": msg})
    # return render(request, "user/register.html")
    # return HttpResponse("<h1>Hello Django! </h1>")
