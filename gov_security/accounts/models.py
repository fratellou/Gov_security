from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class ResourceType(models.Model):
    resource_type = models.CharField(max_length=20)

    def __str__(self):
        return self.resource_type


class Resource(models.Model):
    resource_name = models.CharField(max_length=50)
    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.resource_name


class Position(models.Model):
    position_name = models.CharField(max_length=20)

    def __str__(self):
        return self.position_name


class Permission(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Department(models.Model):
    department_name = models.CharField(max_length=50)
    dep_description = models.TextField()
    emp_num = models.IntegerField()

    def __str__(self):
        return self.department_name


class Head(models.Model):
    head_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.head_name


class Employee(AbstractUser):
    patronymic = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=11, unique=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.TextField()
    head = models.ForeignKey(Head, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name


class TaskList(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_entries')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='task_entries')


User = get_user_model()


class Message(models.Model):
    department = models.ForeignKey(Department, related_name="messages", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def str(self):
        return f"{self.author.username}: {self.message_text[:50]}"
