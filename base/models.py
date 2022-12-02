from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    #on_delete=models.CASCADE means if the user gets deleted, the task remains
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    # we want to automatically populate the time when a task is created
    create = models.DateTimeField(auto_now_add=True)
    
    def __self__(self):
        return self.title
    
    class  Meta:
        ordering = ['complete']