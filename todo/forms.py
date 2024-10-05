from .models import Todo
from django.forms import ModelForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        # fields = "__all__"
        fields = ["title", "text", "date_completed", "important"]
