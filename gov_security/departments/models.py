from django.db import models

from accounts.models import Position


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
