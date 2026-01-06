from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Task(models.Model):

    status = [('in Progress', 'in Progress'), ('completed', 'Completed'), ('To-Do', 'To-do')]
    priority = [('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]

    title = models.CharField(max_length = 20)
    description = models.TextField()
    status = models.CharField(max_length = 15, choices = status, default = 'To-Do')
    priority = models.CharField(max_length = 10, choices = priority, default = 'Medium')
    deadline = models.DateTimeField()
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name = 'tasks')
    def __str__(self):
        return self.title
