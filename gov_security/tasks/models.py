from django.db import models
from profiles.models import Employee
from departments.models import Head


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.TextField()
    head = models.ForeignKey(Head, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name


class TaskList(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='task_entries')
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='task_entries')
