from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from datetime import datetime

# Create your views here.


def delete_todo(request, id):
    user = request.user
    todo = None

    try:
        todo = Todo.objects.get(id=id, user=user)
        todo.delete()

    except Exception as e:
        print(e)

    return redirect("todolist")


# 新增代辦
def create_todo(request):
    msg = ""
    user = request.user
    form = None
    if not user.is_authenticated:
        msg = "請先登入"
    else:
        form = TodoForm()
        if request.method == "POST":
            try:
                print(request.POST)
                form = TodoForm(request.POST)
                todo = form.save(commit=False)
                todo.user = request.user
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                todo.date_completed = now if todo.completed else None
                todo.save()
                msg = "提交成功"
                return redirect("todolist")
            except Exception as e:
                print(e)
                msg = "提交失敗"

    return render(request, "todo/create-todo.html", {"form": form, "msg": msg})


# 檢視代辦
def todo(request, id):
    msg = ""
    user = request.user
    todo = None

    try:
        todo = Todo.objects.get(id=id, user=user)
        form = TodoForm(instance=todo)
        if request.method == "POST":
            form = TodoForm(request.POST, instance=todo)
            todo = form.save(commit=False)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            todo.date_completed = now if todo.completed else None
            todo.save()
            msg = "更新成功"
            return redirect("todolist")

    except Exception as e:
        print(e)
        msg = "編號錯誤"

    return render(request, "todo/todo.html", {"form": form, "todo": todo, "msg": msg})


def todolist(request):

    # 網頁端登入使用者的資訊
    user = request.user
    todos = None
    if user.is_authenticated:
        # 對應資料庫的user
        todos = Todo.objects.filter(user=user)

    print(todos)
    return render(request, "todo/todolist.html", {"todos": todos})


def completed(request):
    user = request.user
    todos = None
    if user.is_authenticated:
        # 對應資料庫的user
        todos = Todo.objects.filter(user=user)

    print(todos)
    return render(request, "todo/completed.html", {"todos": todos})
