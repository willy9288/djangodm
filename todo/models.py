from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
