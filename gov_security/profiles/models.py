from django.db import models
from departments.models import Department
from django.contrib.auth.models import AbstractUser
from accounts.models import Position


class Employee(AbstractUser):
    patronymic = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=11, unique=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
