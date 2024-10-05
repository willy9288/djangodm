from django.shortcuts import render
from .models import Todo

# Create your views here.


def todolist(request):

    # 網頁端登入使用者的資訊
    user = request.user
    todos = None
    if user.is_authenticated:
        # 對應資料庫的user
        todos = Todo.objects.filter(user=user)

    print(todos)
    return render(request, "todo/todolist.html", {"todos": todos})
