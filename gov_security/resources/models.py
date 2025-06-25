from django.db import models


class ResourceType(models.Model):
    resource_type = models.CharField(max_length=20)

    def __str__(self):
        return self.resource_type


class Resource(models.Model):
    resource_name = models.CharField(max_length=50)
    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    resource_file = models.FileField(upload_to='resources/media/')

    def __str__(self):
        return self.resource_name
