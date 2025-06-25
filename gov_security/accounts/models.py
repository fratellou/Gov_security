from django.db import models

from resources.models import Resource


class Position(models.Model):
    position_name = models.CharField(max_length=20)

    def __str__(self):
        return self.position_name


class Permission(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
