from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    msg = ""

    # if request.method == "GET":
    form = UserCreationForm()

    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 比對密碼長度
        if len(password1) != 8 or len(password2) != 8:
            msg = "密碼長度不正確"

        elif password1 != password2:
            msg = "兩次密碼不一樣"

        # 比對密碼是否相同

        # 比對使用者是否存在

        # 註冊使用者

    return render(request, "user/register.html", {"form": form, "msg": msg})
    # return render(request, "user/register.html")
    # return HttpResponse("<h1>Hello Django! </h1>")
