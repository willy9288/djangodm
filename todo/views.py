from django.shortcuts import render
from .models import Todo

# Create your views here.


def todo(request, id):
    msg = ""
    todo = None
    user = request.user
    try:
        todo = Todo.objects.get(id=id, user=user)
    except Exception as e:
        print(e)
        msg = "編號錯誤"

    return render(request, "todo/todo.html", {"todo": todo, "msg": msg})


def todolist(request):

    # 網頁端登入使用者的資訊
    user = request.user
    todos = None
    if user.is_authenticated:
        # 對應資料庫的user
        todos = Todo.objects.filter(user=user)

    print(todos)
    return render(request, "todo/todolist.html", {"todos": todos})
