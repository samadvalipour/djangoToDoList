from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True,blank=True)
    done = models.BooleanField(default=False)

